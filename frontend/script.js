async function uploadPDF() {
  const fileInput = document.getElementById("pdfFile");
  const progress = document.getElementById("progress");
  const audioPlayer = document.getElementById("audioPlayer");

  if (!fileInput.files[0]) {
    alert("Please select a PDF file first.");
    return;
  }

  const formData = new FormData();
  formData.append("file", fileInput.files[0]);

  progress.textContent = "Uploading and converting... ⏳";
  audioPlayer.style.display = "none";

  try {
    const response = await fetch("http://127.0.0.1:8000/convert", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      const err = await response.json();
      throw new Error(err.error || "Failed to convert PDF.");
    }

    const data = await response.json();
    const audioUrl = `http://127.0.0.1:8000/audio/${data.audio_file}`;

    audioPlayer.src = audioUrl;
    audioPlayer.style.display = "block";
    progress.textContent = "✅ Conversion complete! Ready to play.";
  } catch (error) {
    console.error(error);
    progress.textContent = "❌ Something went wrong: " + error.message;
  }
}
