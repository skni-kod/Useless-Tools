pipeline{
    agent none
    environment {
        REGISTRY = 'harbor.skni.edu.pl/'
        DOCKER_REGISTRY_CREDENTIALS_ID = 'harbor'
        IMAGE = 'harbor.skni.edu.pl/library/ut'
    }
    stages{
        stage('Stash'){
            steps{
                stash name: 'source', includes: '**'
            }
        }
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
                unstash 'source'
                container('sonarqube') {
                    withCredentials([string(credentialsId: 'sonar', variable: 'TOKEN')]) {
                        sh """sonar-scanner -Dsonar.organization=$ORGANIZATION \
                            -Dsonar.projectKey=$PROJECT_NAME \
                            -Dsonar.host.url=$SONAR_SERVER \
                            -Dsonar.login=your-$TOKEN \
                            -Dsonar.sources=. \
                            -Dsonar.sourceEncoding=UTF-8 \
                            -Dsonar.language=python \
                            -Dsonar.python.version=3.10
                        """
                    }
                }
            }
        }
//        stage('Scan source') {
//	    agent{
//                label 'host'
//            }
//            steps {
//                // Scan all vuln levels
//                sh 'mkdir -p reports'
//                sh 'trivy filesystem --ignore-unfixed --vuln-type os,library --format json -o reports/python.json .'
//                // Scan again and fail on CRITICAL vulns
//                sh 'trivy filesystem --ignore-unfixed --vuln-type os,library --exit-code 1 --severity CRITICAL .'
//		        archiveArtifacts 'reports/python.json'
//            }
//        }
//        stage('Build Back'){
//            agent{
//                label 'host'
//            }
//            steps{
//                    sh """
//                    docker build -t $IMAGE:$BUILD_ID .
//                    """
//            }
//        }
//        stage('Push to registry - back'){
//            agent{
//                label 'host'
//            }
//            steps{
//                withCredentials([usernamePassword(credentialsId: 'harbor', passwordVariable: 'passwd', usernameVariable: 'username')]) {
//                    sh """
//                    docker login -u $username -p $passwd  ${env.REGISTRY}
//                       docker push $IMAGE:$BUILD_ID
//                       docker tag $IMAGE:$BUILD_ID $IMAGE:latest
//                       docker push $IMAGE:latest
//                       docker image rm $IMAGE:latest
//                       docker image rm $IMAGE:$BUILD_ID
//                    """
//                }
//            }
//        }
//	    stage('Update k8s config') {
//            agent{
//                label 'host'
//            }
//            steps {
//		sh 'sed -i "s|harbor.skni.edu.pl/library/ut:latest|harbor.skni.edu.pl/library/ut:${BUILD_ID}|g" k8s/app-deployment.yaml'
//        	sh 'sed -i "s|harbor.skni.edu.pl/library/ut:latest|harbor.skni.edu.pl/library/ut:${BUILD_ID}|g" k8s/db-migration-job.yaml'
//                stash name: 'kubernetes', includes: 'k8s/**'
//            }
//        }
//        stage('Deploy'){
//            agent {
//	        docker {
//	            image 'bitnami/kubectl:latest'
//	            args "--entrypoint=''"
//	        }
//	    }
//            steps{
//		        unstash 'kubernetes'
//                withCredentials([file(credentialsId: 'k8s-kubeconfig', variable: 'CONFIG')]) {
//                        sh """
//        	    		    mv k8s/* .
//                            kubectl --kubeconfig=$CONFIG delete job --ignore-not-found=true -n useless-tools ut-migration
//        	    		    kubectl --kubeconfig=$CONFIG apply -f db-migration-job.yaml
//        	    		    kubectl --kubeconfig=$CONFIG apply -f app-deployment.yaml
//        	    		    kubectl --kubeconfig=$CONFIG apply -f app-service.yaml
//        	    		    kubectl --kubeconfig=$CONFIG apply -f ingress.yaml
//                  		"""
//                }
//            }
//        }
//    }
//    post {
//        always {
//            node('host') {
//                deleteDir()
//            }
//        }
    }
}
