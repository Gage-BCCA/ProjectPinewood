class DocumentObject {
    constructor(type, order, content) {
        this.type = type;
        this.order = order;
        this.content = content;
    }
}

// Grab all buttons
const addBigHeaderBtn = document.getElementById("add-big-header-btn");
const addSmallHeaderBtn = document.getElementById("add-small-header-btn");
const addTextSectionBtn = document.getElementById("add-text-section-btn");
const submitBtn = document.getElementById("submit-btn");
const documentElement = document.getElementById("document");

// Title Input Boxes
const titleInputBox = document.getElementById("title-input-box");
const subtitleInputBox = document.getElementById("subtitle-input-box");

// Document state variables
let currentDocumentPosition = 0;
let documentElementList = new Array();
let postTitle = titleInputBox.value;
let postSubtitle = subtitleInputBox.value;

// Placeholder text for different elements
const bigHeaderText = `Big Header`;
const smallHeaderText = `Small Header`;
const textSectionText = `Text section`;

// Add event listeners
addBigHeaderBtn.addEventListener("click", addBigHeaderToDocument);
addSmallHeaderBtn.addEventListener("click", addSmallHeaderToDocument);
addTextSectionBtn.addEventListener("click", addTextSectionToDocument);
submitBtn.addEventListener("click", savePost);

titleInputBox.addEventListener("input", function() {
    postTitle = titleInputBox.value;
});

subtitleInputBox.addEventListener("input", function() {
    postSubtitle = subtitleInputBox.value;
});

// Grab existing elements in the document div in
// the case that some already exist (i.e., if we
// are editing a post instead of creating
document.addEventListener("DOMContentLoaded", function () {
console.log(documentElement.children)
    for(let child of documentElement.children) {
        currentDocumentPosition += 1;
        let target = child.firstElementChild;
        target.contentEditable = true;
        if (target.nodeName == "H1") {
            documentElementList.push(
                new DocumentObject(
                "bigHeader",
                currentDocumentPosition,
                target.textContent
                )
            );
        }
        else if (target.nodeName == "H2") {
            documentElementList.push(
                new DocumentObject(
                "smallHeader",
                currentDocumentPosition,
                target.textContent
                )
            );
        }
        else if (target.nodeName == "P") {
            documentElementList.push(
                new DocumentObject(
                "textSection",
                currentDocumentPosition,
                target.textContent
                )
            );
        }
    }
    console.log(documentElementList);
});

function addTextSectionToDocument() {
    let newDiv = document.createElement('div');
    let textSection = document.createElement('p');
    textSection.textContent = textSectionText;
    textSection.classList.add("text-section");
    newDiv.appendChild(textSection);
    newDiv.tabIndex = 1;
    textSection.contentEditable = true;
    textSection.addEventListener("click", function () {
        this.focus();
    });

    textSection.addEventListener("focusout", function () {
        for (let element of documentElementList) {
            if (element.order == this.parentNode.dataset.order) {
                element.content = this.textContent;
                console.log(element.content);
                break;
            }
        }

    });
    documentElement.appendChild(newDiv);
    currentDocumentPosition += 1;
    documentElementList.push(
        new DocumentObject(
            "textSection",
            currentDocumentPosition,
            newDiv.firstElementChild.textContent
        )
    );
    newDiv.dataset.order = currentDocumentPosition;
}

function addSmallHeaderToDocument() {
    let newDiv = document.createElement('div');
    let newHeader = document.createElement('h2');
    newHeader.textContent = smallHeaderText;
    newHeader.classList.add("small-header");
    newDiv.appendChild(newHeader);
    newDiv.tabIndex = 1;
    newHeader.contentEditable = true;
    newHeader.addEventListener("click", function () {
        this.focus();
    });

    newHeader.addEventListener("focusout", function () {
        for (let element of documentElementList) {
            if (element.order == this.parentNode.dataset.order) {
                element.content = this.textContent;
                console.log(element.content);
                break;
            }
        }

    });
    documentElement.appendChild(newDiv);
    currentDocumentPosition += 1;
    documentElementList.push(
        new DocumentObject(
            "smallHeader",
            currentDocumentPosition,
            newDiv.firstElementChild.textContent
        )
    );
    newDiv.dataset.order = currentDocumentPosition;
}

function addBigHeaderToDocument() {
    let newDiv = document.createElement('div');
    let newHeader = document.createElement('h1');
    newHeader.textContent = bigHeaderText;
    newHeader.classList.add("big-header");
    newDiv.appendChild(newHeader);
    newDiv.tabIndex = 1;
    newHeader.contentEditable = true;
    newHeader.addEventListener("click", function () {
        this.focus();
    });

    newHeader.addEventListener("focusout", function () {
        for (let element of documentElementList) {
            if (element.order == this.parentNode.dataset.order) {
                element.content = this.textContent;
                console.log(element.content);
                break;
            }
        }
    });
    documentElement.appendChild(newDiv);
    currentDocumentPosition += 1;
    documentElementList.push(
        new DocumentObject(
            "bigHeader",
            currentDocumentPosition,
            newDiv.firstElementChild.textContent
        )
    );
    newDiv.dataset.order = currentDocumentPosition;
}

function savePost() {
    let url;
    if (documentElement.hasAttribute("data-post-id"))
    {
        url = "/management/api/blog/save"
        data = {
            title: postTitle,
            subtitle: postSubtitle,
            body: documentElementList,
            id: documentElement.dataset.postId
        }
    }
    else {
        url = "/management/api/blog/new"
        data = {
            title: postTitle,
            subtitle: postSubtitle,
            body: documentElementList,
        }
    }

    fetch(url, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken')
    },
    body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok)
        {

        }
    })
    .catch(error => {
        console.error("Error")
    });
}


// Function to get CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}