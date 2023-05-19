pipeline{
    agent none
    environment {
        REGISTRY = 'harbor.skni.edu.pl/'
        DOCKER_REGISTRY_CREDENTIALS_ID = 'harbor'
        IMAGE = 'harbor.skni.edu.pl/library/ut'
    }
    stages{
        stage('Sonar'){
            agent{
                label 'sonar'
            }
            environment {
                ORGANIZATION = "SKNI-KOD"
                PROJECT_NAME = "Useless-tools"
                SONAR_SERVER = "https://sonar.skni.edu.pl"
            }
            steps{
                container('sonarqube') {
                    withCredentials([string(credentialsId: 'sonar', variable: 'TOKEN')]) {
                        sh """sonar-scanner -Dsonar.organization=$ORGANIZATION \
                            -Dsonar.projectKey=$PROJECT_NAME \
                            -Dsonar.host.url=$SONAR_SERVER \
                            -Dsonar.login=$TOKEN \
                            -Dsonar.sources=. \
                            -Dsonar.exclusions=./helm/**/* \
                            -Dsonar.sourceEncoding=UTF-8 \
                            -Dsonar.language=python \
                            -Dsonar.python.version=3.10
                        """
                    }
                }
            }
        }
        stage('Scan source') {
	        agent{
                label 'trivy'
            }
            steps {
                container('trivy'){
                    withCredentials([file(credentialsId: 'junit.tpl', variable: 'TEMPLATE')]) {
                        sh "cp $TEMPLATE junit.tpl"
                    }
                    // Scan all vuln levels
                    sh 'trivy filesystem --ignore-unfixed --vuln-type os,library --format template --template "junit.tpl" -o report-app.xml .'
                    // Scan again and fail on CRITICAL vulns
                    sh 'trivy filesystem --ignore-unfixed --vuln-type os,library --exit-code 1 --severity CRITICAL .'
		            stash includes: 'report-app.xml', name: 'report-app'
                }
            }
        }
        stage('Build'){
            agent{
                label 'kaniko'
            }
            steps{
                container('kaniko'){
                    sh "/kaniko/executor --context=\$(pwd) --dockerfile=\$(pwd)/Dockerfile --cache=true --destination=$IMAGE:$BUILD_ID"
                }
            }
        }
        stage('Scan image') {
            agent{
                label 'trivy'
            }
            steps {
                container('trivy'){
                    withCredentials([usernamePassword(credentialsId: 'harbor', passwordVariable: 'PASSWD', usernameVariable: 'USER')]) {
                        withCredentials([file(credentialsId: 'junit.tpl', variable: 'TEMPLATE')]) {
                            sh "cp $TEMPLATE junit.tpl"
                        }
                        // Scan all vuln levels
                        sh 'trivy image --format template --template "junit.tpl" -o report-image.xml --username $USER --password $PASSWD $IMAGE:$BUILD_ID'
                        // Scan again and fail on CRITICAL vulns
                        sh "trivy image --exit-code 1 --severity CRITICAL --username $USER --password $PASSWD  $IMAGE:$BUILD_ID"
		                stash includes: 'report-image.xml', name: 'report-image'
                    }
                }
            }
        }
        stage('Generate reports'){
            agent{
                label 'ant'
            }
            steps{
                container('ant'){
                    unstash 'report-app'
                    unstash 'report-image'
                    sh 'mkdir reports'
                    sh 'ant -f /build.xml'
                    archiveArtifacts 'reports/html/*'
                }
            }
        }
        stage('Deploy'){
            agent {
                label 'helm'
	        }
            steps{
        		container(name: 'helm', shell: '/bin/sh') {
                    withCredentials([file(credentialsId: 'k8s-ca', variable: 'MY_CA'), string(credentialsId: 'k8s-token', variable: 'MY_TOKEN')]) { 
                    sh """
                        kubectl config set-cluster mycluster --server=https://kubernetes.default --certificate-authority=${MY_CA}
                        kubectl config set-credentials jenkins-robot --token=${MY_TOKEN}
                        kubectl config set-context mycontext --cluster=mycluster --user=jenkins-robot
                        kubectl config use-context mycontext
                        helm upgrade --install --namespace useless-tools --set image.tag=${BUILD_ID} useless-tools ./helm
                    """
                    }
                }
            }
        }
//    post {
//        always {
//            node('host') {
//                deleteDir()
//            }
//        }
    }
}
