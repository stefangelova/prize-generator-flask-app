pipeline{
        agent any
        stages{
            stage('Deploy App'){
                steps{
                    sh """
                    ssh stef@51.104.16.150 << EOF
                    rm -rf project2
                    git clone https://github.com/stefangelova/project2.git
                    cd project2
                    export DATABASE_URI=mysql+pymysql://root:mypassword@mysqldb/proj2db
                    export SECRET_KEY=secretkey
                    sudo docker-compose up -d
                    """
               }
            }
        }    
}
