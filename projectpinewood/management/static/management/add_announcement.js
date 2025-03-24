const callToActionCheckbox = document.getElementById("call-to-action-checkbox");
const callToActionContainer = document.getElementById("call-to-action-container");

const expiryDateCheckbox = document.getElementById("expiry-checkbox");
const expiryDateContainer = document.getElementById("expiry-date-container");

callToActionCheckbox.addEventListener("click", function (event) {
    if (callToActionCheckbox.checked) {
        callToActionContainer.style.display = "block";
    }
    else {
        callToActionContainer.style.display = "none";
    }
});

expiryDateCheckbox.addEventListener("click", function (event) {
    if (expiryDateCheckbox.checked) {
        expiryDateContainer.style.display = "block";
    }
    else {
        expiryDateContainer.style.display = "none";
    }
})

document.addEventListener("DOMContentLoaded", function (event) {
    callToActionContainer.style.display = "none";
    expiryDateContainer.style.display = "none";
})