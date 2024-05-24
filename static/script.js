document.getElementById('tellMeButton').addEventListener('click', function() {
    submitForm('Tell Me About the Resume');
});

document.getElementById('percentageMatchButton').addEventListener('click', function() {
    submitForm('Percentage match');
});

function submitForm(action) {
    var formData = new FormData(document.getElementById('uploadForm'));
    formData.append('action', action);

    fetch('/evaluate', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.response) {
            // Replace \n with <br>
            const formattedResponse = data.response.replace(/\n/g, '<br>');
            document.getElementById('responseContainer').innerHTML = formattedResponse;
        } else {
            document.getElementById('responseContainer').innerHTML = "An error occurred: " + data.error;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('responseContainer').innerHTML = "An unexpected error occurred.";
    });
}


const scriptURL = 'https://script.google.com/macros/s/AKfycbw-GUGjpFuzSZiMCTAUcmpx5X90zvVDzy_NaZd19pEqP8Iyi06VNdL8rs72nQyIufOuEA/exec'
    const form = document.forms['submit-to-google-sheet']
    const msg =document.getElementById("msg")

    form.addEventListener('submit', e => {
      e.preventDefault()
      fetch(scriptURL, { method: 'POST', body: new FormData(form)})
        .then(response => {
            msg.innerHTML = "Message sent successfully"
            setTimeout(function(){
                msg.innerHTML =""
            },5000)
            form.reset()
        })
        .catch(error => console.error('Error!', error.message))
    })

// document.addEventListener("DOMContentLoaded", () => {
//     const authButton = document.getElementById('auth-button');
    
//     // Simulate user authentication state
//     const isAuthenticated = false; // Change this to true if the user is logged in

//     if (isAuthenticated) {
//         authButton.innerHTML = '<a href="profile.html">Profile</a>'; // Link to the user's profile page
//     } else {
//         authButton.innerHTML = '<a href="login.html">Login/Register</a>'; // Link to the login/register page
//     }
// });




// $(document).ready(function() {
//     $('#tellMeButton').click(function(event) {
//         event.preventDefault();
//         submitForm('Tell Me About the Resume');
//     });

//     $('#percentageMatchButton').click(function(event) {
//         event.preventDefault();
//         submitForm('Percentage match');
//     });

//     function submitForm(action) {
//         let formData = new FormData();
//         formData.append('input_text', $('#input_text').val());
//         formData.append('file', $('#file')[0].files[0]);
//         formData.append('action', action);

//         $.ajax({
//             url: '/evaluate',
//             type: 'POST',
//             data: formData,
//             processData: false,
//             contentType: false,
//             success: function(response) {
//                 $('#responseContainer').html('<pre>' + JSON.stringify(response, null, 2) + '</pre>');
//             },
//             error: function(xhr, status, error) {
//                 $('#responseContainer').html('<pre>Error: ' + xhr.responseText + '</pre>');
//             }
//         });
//     }
// });
