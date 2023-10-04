
document.addEventListener('DOMContentLoaded', function () {
    // Get all buttons somehow, you could give them a more meaningful class name than bn49
    let buttons = document.querySelectorAll(".bn49");

    // Give every button an event listener
    buttons.forEach((button) => {
        // Do some logic to check whether the button answer is correct
        if (button.classList.contains("correct")) {
            // Create a click event listener with whatever reaction you desire.
            button.addEventListener('click', function () {
                button.style.backgroundColor = 'green';
            })
        }
        else {
            button.addEventListener('click', function () {
                // And a different one for incorrect answers
                button.style.backgroundColor = 'red';
            })
        }
    })
})