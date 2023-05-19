pipeline{
    agent none
    environment {
        REGISTRY = 'harbor.skni.edu.pl/'
        DOCKER_REGISTRY_CREDENTIALS_ID = 'harbor'
        IMAGE = 'harbor.skni.edu.pl/library/ut'
    }
    stages{
//        stage('Sonar'){
//            agent{
//                label 'sonar'
//            }
//            environment {
//                ORGANIZATION = "SKNI-KOD"
//                PROJECT_NAME = "Useless-tools"
//                SONAR_SERVER = "https://sonar.skni.edu.pl"
//            }
//            steps{
//                container('sonarqube') {
//                    withCredentials([string(credentialsId: 'sonar', variable: 'TOKEN')]) {
//                        sh """sonar-scanner -Dsonar.organization=$ORGANIZATION \
//                            -Dsonar.projectKey=$PROJECT_NAME \
//                            -Dsonar.host.url=$SONAR_SERVER \
//                            -Dsonar.login=$TOKEN \
//                            -Dsonar.sources=. \
//                            -Dsonar.sourceEncoding=UTF-8 \
//                            -Dsonar.language=python \
//                            -Dsonar.python.version=3.10
//                        """
//                    }
//                }
//            }
//        }
        stage('Scan source') {
	        agent{
                label 'trivy'
            }
            steps {
                container('trivy'){
                    // Scan all vuln levels
                    sh 'mkdir -p reports'
                    sh 'trivy filesystem --ignore-unfixed --vuln-type os,library --format json -o reports/python.json .'
                    // Scan again and fail on CRITICAL vulns
                    sh 'trivy filesystem --ignore-unfixed --vuln-type os,library --exit-code 1 --severity CRITICAL .'
		            archiveArtifacts 'reports/python.json'
                }
            }
        }
        stage('Build'){
            agent{
                label 'kaniko'
            }
            steps{
                container('kaniko'){
                    sh "/kaniko/executor --context=\$(pwd) --dockerfile=\$(pwd)/Dockerfile --destination=$IMAGE:$BUILD_ID"
                }
            }
        }
        stage('Deploy'){
            agent {
                label 'kubectl'
	        }
            steps{
		container(name: 'kubectl', shell: '/bin/sh') {
			sh 'echo dupa'
                    dir('k8s'){
                        withCredentials([file(credentialsId: 'k8s-ca', variable: 'MY_CA'), string(credentialsId: 'k8s-token', variable: 'MY_TOKEN')]) { 
                        sh """
                            sed -i "s|harbor.skni.edu.pl/library/ut:imagetag|harbor.skni.edu.pl/library/ut:${BUILD_ID}|g" app-deployment.yaml
                            sed -i "s|harbor.skni.edu.pl/library/ut:imagetag|harbor.skni.edu.pl/library/ut:${BUILD_ID}|g" db-migration-job.yaml
                            kubectl config set-cluster mycluster --server=https://kubernetes.default --certificate-authority=${MY_CA}
                            kubectl config set-credentials jenkins-robot --token=${MY_TOKEN}
                            kubectl config set-context mycontext --cluster=mycluster --user=jenkins-robot
                            kubectl config use-context mycontext
                            kubectl  delete job --ignore-not-found=true -n useless-tools ut-migration
                	    	kubectl  apply -f db-migration-job.yaml
                	    	kubectl  apply -f app-deployment.yaml
                	    	kubectl  apply -f app-service.yaml
            	         	kubectl  apply -f ingress.yaml
                        """
                        }
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
