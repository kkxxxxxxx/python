import boto3
import os

# 需要修改的参数
AWS_ACCESS_KEY_ID=""
AWS_SECRET_ACCESS_KEY=""
AWS_REGION=""
AWS_S3_BUCKET=""
AWS_S3_DIR=""   # S3 目标目录
LOCAL_FILE_PATH=""   # 本地文件路径
LOCAL_FILE_NAME= os.path.basename(LOCAL_FILE_PATH)  # 保留原文件名

# 构造 S3 对象 Key
KEY_NAME = f"{AWS_S3_DIR}/{LOCAL_FILE_NAME}"

# 创建 S3 客户端
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

   # 上传文件并设置 ACL 为 public-read
s3.upload_file(LOCAL_FILE_PATH, AWS_BUCKET, KEY_NAME, ExtraArgs={'ACL': 'public-read'})

# 生成公共访问地址
url = f"https://{AWS_S3_BUCKET}.s3.{AWS_S3_REGION}.amazonaws.com/{KEY_NAME}"
print("✅ 上传成功!")
print("📂 S3 对象路径:", f"s3://{AWS_S3_BUCKET}/{KEY_NAME}")
print("🌍 公共访问地址:", url)
