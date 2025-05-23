const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const captureBtn = document.getElementById('capture');
const responseText = document.getElementById('response');

// Solicitar acceso a la cámara
navigator.mediaDevices.getUserMedia({ video: true })
  .then(stream => {
    video.srcObject = stream;
  })
  .catch(err => {
    console.error("Error al acceder a la cámara: ", err);
  });

captureBtn.addEventListener('click', () => {
  const context = canvas.getContext('2d');
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;

  context.drawImage(video, 0, 0, canvas.width, canvas.height);
  canvas.toBlob(blob => {
    const formData = new FormData();
    formData.append('image', blob, 'captura.jpg');

    fetch('http://localhost:5000/upload', {
      method: 'POST',
      body: formData
    })
    .then(res => res.json())
    .then(data => {
      responseText.textContent = `Nombre: ${data.name}, Confianza: ${data.confidence}`;
    })
    .catch(err => {
      console.error("Error en el reconocimiento: ", err);
      responseText.textContent = "Ocurrió un error.";
    });
  }, 'image/jpeg');
});
