function openModal() {
  document.getElementById("modal").style.display = "block";
}

function closeModal() {
  document.getElementById("modal").style.display = "none";
}

async function submitBook(event) {
  event.preventDefault();

  const form = event.target;
  const formData = new FormData(form);

  await fetch("/api/book", {
    method: "POST",
    body: formData,
  });

  form.reset();
  closeModal();
  location.reload();
}

async function deleteBook(bookId) {
  await fetch(`/api/book/${bookId}`, {
    method: "DELETE",
  });
  location.reload();
}
