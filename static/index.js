const headline = document.getElementById('headline');
  window.addEventListener('scroll', () => {
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    if (scrollTop > 150) {
      headline.classList.add('scrolled');
    } else {
      headline.classList.remove('scrolled');
    }
  });


 function sendEmail(choice) {
      showToast(`✅ Sending ${choice}`);
      fetch("/send-email", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          choice: choice
        })
      })
      .then(res => res.json())
      .then(data => alert(data.message))
      .catch(err => alert("Error sending choice."));
    }

    function showToast(message) {
    const toast = document.getElementById("toast");
    toast.textContent = message;
    toast.classList.add("show");

    setTimeout(() => {
      toast.classList.remove("show");
    }, 3000); // Toast disappears after 3 seconds
  }

  



  