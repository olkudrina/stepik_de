### command to run aws glue

docker run -it \
-v ~/.aws:/home/glue_user/.aws \
-v glue_workspace:/home/glue_user/workspace/jupyter_workspace/ \
-e AWS_ACCESS_KEY_ID=$(aws configure get aws_access_key_id) \
-e AWS_SECRET_ACCESS_KEY=$(aws configure get aws_secret_access_key) \
-e DISABLE_SSL=true \
--rm -p 4040:4040 -p 18080:18080 -p 8998:8998 -p 8888:8888 \
--name glue_jupyter_lab \
amazon/aws-glue-libs:glue_libs_4.0.0_image_01 \
/home/glue_user/jupyter/jupyter_start.sh

### separate command to install faker
docker exec -it glue_jupyter_lab pip3 install faker