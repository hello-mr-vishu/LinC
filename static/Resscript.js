// Function to add a new Work Experience field
function addNewWEField() {
    let newNode = document.createElement('textarea');
    newNode.classList.add('form-control', 'weField', 'mt-2');
    newNode.setAttribute('placeholder', 'Enter Here');
    newNode.setAttribute("rows", 3);

    let weOb = document.getElementById("we");
    let weAddButtonOb = document.getElementById("weAddButton");

    weOb.insertBefore(newNode, weAddButtonOb);
}

// Function to add a new Academic Qualification field
function addNewAQField() {
    let newNode = document.createElement('textarea');
    newNode.classList.add('form-control', 'eqField', 'mt-2');
    newNode.setAttribute('placeholder', 'Enter Here');
    newNode.setAttribute("rows", 3);

    let aqOb = document.getElementById("aq");
    let aqAddButtonOb = document.getElementById("aqAddButton");

    aqOb.insertBefore(newNode, aqAddButtonOb);
}
// Function to generate the CV
function generateCV() {
    // Personal Information
    let nameField = document.getElementById('nameField').value;
    document.getElementById('nameT1').innerHTML = nameField;
    document.getElementById('nameT2').innerHTML = nameField;

    document.getElementById("contactT").innerHTML = document.getElementById("contactField").value;
    document.getElementById("addressT").innerHTML = document.getElementById("addressField").value;
    document.getElementById("fbT").innerHTML = document.getElementById("facebookField").value;
    document.getElementById("instaT").innerHTML = document.getElementById("instaField").value;
    document.getElementById("linkedT").innerHTML = document.getElementById("linkedField").value;

    // Objective
    document.getElementById("objectiveT").innerHTML = document.getElementById("objectiveField").value;

    // Work Experience
    let wes = document.getElementsByClassName("weField");
    let weStr = "";
    for (let e of wes) {
        if (e.value.trim() !== "") {
            weStr += `<li>${e.value}</li>`;
        }
    }
    document.getElementById("weT").innerHTML = weStr;

    // Academic Qualifications
    let aqs = document.getElementsByClassName("eqField");
    let aqStr = "";
    for (let e of aqs) {
        if (e.value.trim() !== "") {
            aqStr += `<li>${e.value}</li>`;
        }
    }
    document.getElementById("aqT").innerHTML = aqStr;
    
    let file = document.getElementById('imgField').files[0];
    if (file) {
        let reader = new FileReader();
        reader.readAsDataURL(file);

        reader.onloadend = function () {
            document.getElementById('imgTemplate').src = reader.result;
        };
    }



    document.getElementById('cv-form').style.display='none';
    document.getElementById('header').style.display='none';
    document.getElementById("cv-template").style.display="black";

}


function printCV(){
    window.print();
}