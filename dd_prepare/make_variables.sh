#!/bin/bash

echo $CI_JOB_TOKEN
FILENAME='security_variables.env'
rm $FILENAME 2>/dev/null
touch $FILENAME

echo "DEPCHECK_MYSQL='Insert_HERE_MYSQL_PASSWORD'"                               >> $FILENAME
echo 'TRIVY_TOKEN="INSERT_HERE_TRIVY_RANDOM_TOKEN"'                                 >> $FILENAME
##################
### juice_shop ###
##################
if [[ $PROJECT_PATH == "test/juice-shop" ]]
then
    echo APPSEC_DOCKERFILE=Dockerfile                                                                        >> $FILENAME
    echo APPSEC_CONTAINER=${SEC_CI_REGISTRY_IMAGE}/${SEC_CI_COMMIT_REF_NAME}                                 >> $FILENAME

##################
### juice_shop2 ###
##################
elif [[ $PROJECT_PATH == "test/juice-shop2" ]]
then
    echo APPSEC_DOCKERFILE=Dockerfile                                                                        >> $FILENAME
    echo APPSEC_CONTAINER=${SEC_CI_REGISTRY_IMAGE}/${SEC_CI_COMMIT_REF_NAME}                                 >> $FILENAME


##############
### FINISH ###
##############
else
  APPSEC_DOCKERFILE="" >> $FILENAME
  APPSEC_CONTAINER=""  >> $FILENAME
  echo "No variables for this project yet, will be soon."
fi

cat $FILENAME
