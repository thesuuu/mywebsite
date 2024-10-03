document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('upload-form');  
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', function(event) {
        event.preventDefault();  // 阻止表单的默认提交行为

        const formData = new FormData(form);
        fetch('/process_image', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            if (data.success) {
                // 清空之前的提示信息
                resultDiv.innerHTML = '';

                // 创建下载链接并插入到DOM中
                const downloadLink = document.createElement('a');
                downloadLink.href = data.url;
                downloadLink.textContent = 'Download Processed Image';
                downloadLink.download = true;
                resultDiv.appendChild(downloadLink);
            } else {
                resultDiv.innerHTML = '<p>Error: ' + data.message + '</p>';
            }
        })
        .catch(error => {
            console.error('Error:', error);
            resultDiv.innerHTML = '<p>Error: An unexpected error occurred.</p>';
        });
    });
});