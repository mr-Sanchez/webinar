
window.onload = function() {
  // show an upload file name - <START>

  const fileUpload = document.querySelector('#file-upload');
  const fileChosen = document.querySelector('#file-chosen');
  
  fileUpload.addEventListener('change', function(){
    fileChosen.textContent = this.files[0].name
  })

  // show an upload file name - <END>

  submitButton = document.querySelector('.btn-submit');
  formElem = document.querySelector('#upload-form');

  submitButton.onclick = async (e) => {
    e.preventDefault();

    let response = await fetch('/tools/excel_db_prepare', {
      method: 'POST',
      body: new FormData(formElem)
    });

    let result = await response.json();
    if (result.status == '200_OK') {
      //formElem.reset()
      alert('fix me')
    }
  };

  uploadContainer = document.querySelector('.label-file-upload');
  uploadContainer.onmouseover = uploadContainer.onmouseout = handler;

  function handler(event) {
    chooseFileText = document.querySelector('#choose-file-text');
    chooseFileIcon = document.querySelector('.fa-cloud-upload-alt');
    if (event.type == 'mouseover') {
      //chooseFileText.style.display = 'none';
      chooseFileIcon.style.display = 'inline';
    }
    if (event.type == 'mouseout') {
      //chooseFileText.style.display = 'inline';
      chooseFileIcon.style.display = 'none';
    }
  }
}

