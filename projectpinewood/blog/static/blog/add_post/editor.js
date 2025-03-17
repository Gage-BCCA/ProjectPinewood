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
const documentElement = document.getElementById("document");

// Document state variables
let currentDocumentPosition = 0;
let documentElementList = new Array();

// Placeholder text for different elements
const bigHeaderText = `Big Header`;
const smallHeaderText = `Small Header`;
const textSectionText = `Text section`;

// Add event listeners
addBigHeaderBtn.addEventListener("click", addBigHeaderToDocument);
addSmallHeaderBtn.addEventListener("click", addSmallHeaderToDocument);
addTextSectionBtn.addEventListener("click", addTextSectionToDocument);

function addTextSectionToDocument()  {
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





