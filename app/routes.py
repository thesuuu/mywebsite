from flask import Blueprint, request, jsonify, send_from_directory, render_template
from werkzeug.utils import secure_filename
import os
from PIL import Image

bp = Blueprint('main', __name__)

# 设置上传和处理文件的目录
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'app/uploads')
PROCESSED_FOLDER = os.path.join(os.getcwd(), 'app/processed')

# 确保这两个目录存在
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

def handle_uploaded_file(file, filename):
    """
    处理上传的文件，包括保存、处理和返回处理后的文件路径。
    """
    if file.filename == '':
        return {'success': False, 'message': 'No selected file'}, 400

    filename = secure_filename(filename)
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)

    try:
        # 图像处理逻辑
        img = Image.open(file_path)
        img = img.convert("L")  # 示例：转换为灰度图
        processed_file_path = os.path.join(PROCESSED_FOLDER, filename)
        img.save(processed_file_path)

        # 返回处理后的文件路径
        return {'success': True, 'processed_file_path': processed_file_path}, 200
    except Exception as e:
        # 清理临时文件
        os.remove(file_path)
        return {'success': False, 'message': str(e)}, 500

@bp.route('/')
def index():
    result_url = None
    return render_template('index.html', result_url=result_url)

@bp.route('/process_image', methods=['POST'])
def process_image():
    if 'file' not in request.files:
        return jsonify({'success': False, 'message': 'No file part'}), 400
    
    file = request.files['file']
    result, code = handle_uploaded_file(file, file.filename)
    if result['success']:
        processed_file_path = result['processed_file_path']
        url = f"/processed/{os.path.basename(processed_file_path)}"
        return jsonify({'success': True, 'url': url}), 200
    else:
        return jsonify(result), code
    
@bp.route('/processed/<path:filename>')
def download_processed(filename):
    file_path = os.path.join(PROCESSED_FOLDER, filename)
    if not os.path.exists(file_path):
        return jsonify({'success': False, 'message': 'File not found'}), 404

    return send_from_directory(PROCESSED_FOLDER, filename, as_attachment=True)