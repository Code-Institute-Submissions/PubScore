// Function for sending a mail to the owner of the website and clearing the form after that.
// Returns a message to let the user know if the mail was send succesfully
function sendMail(contactForm) {
    try {
        emailjs.send("gmail", "PubScore", {
            "from_name": contactForm.name.value,
            "from_email": contactForm.email.value,
            "message": contactForm.message.value
        });
        $("#name, #email, #message").val("");
        alert("Thank you for your message!");
        return true;
    } catch (error) {
        $("#name, #email, #message").val("");
        alert("Something went wrong. Please try again later.");
        return false;
    }
}