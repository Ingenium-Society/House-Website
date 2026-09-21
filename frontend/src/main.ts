const messageElement = document.querySelector<HTMLHeadingElement>("#message");

async function getMessage() {
  const response = await fetch("http://127.0.0.1:5000/api/hello");

  const data: { message: string } = await response.json();

  if (messageElement) {
    messageElement.textContent = data.message;
  }
}

getMessage();
