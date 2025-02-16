class Book {
    constructor(title, author, read = false) {
        this.title = title;
        this.author = author;
        this.read = read;
    }
}
  
const books = [
    new Book('To Kill a Mockingbird', 'Harper Lee'),
    new Book('1984', 'George Orwell'),
    new Book('The Great Gatsby', 'F. Scott Fitzgerald')
];
  
const library = JSON.parse(localStorage.getItem('library')) || [];
  
function renderBooks() {
    const bookList = document.getElementById('bookList');
    bookList.innerHTML = '';
    books.forEach((book, index) => {
        const bookElement = document.createElement('div');
        bookElement.classList.add('book');
        bookElement.innerHTML = `
            <h3>${book.title}</h3>
            <p>${book.author}</p>
            <button onclick="addToLibrary(${index})">Add to Library</button>
        `;
        bookList.appendChild(bookElement);
    });
}
  
function renderLibrary() {
    const libraryList = document.getElementById('libraryList');
    libraryList.innerHTML = '';
    library.forEach((book, index) => {
        const libraryElement = document.createElement('div');
        libraryElement.classList.add('library-item');
        libraryElement.innerHTML = `
            <h3>${book.title}</h3>
            <p>${book.author}</p>
            <p>${book.read ? 'Read' : 'Unread'}</p>
            <button onclick="toggleRead(${index})">${book.read ? 'Mark as Unread' : 'Mark as Read'}</button>
            <button onclick="removeFromLibrary(${index})">Remove from Library</button>
        `;
        libraryList.appendChild(libraryElement);
    });
}
  
function addToLibrary(bookIndex) {
    const book = books[bookIndex];
    library.push(book);
    localStorage.setItem('library', JSON.stringify(library));
    renderLibrary();
}
  
function removeFromLibrary(libraryIndex) {
    library.splice(libraryIndex, 1);
    localStorage.setItem('library', JSON.stringify(library));
    renderLibrary();
}
  
function toggleRead(libraryIndex) {
    library[libraryIndex].read = !library[libraryIndex].read;
    localStorage.setItem('library', JSON.stringify(library));
    renderLibrary();
}
  
document.addEventListener('DOMContentLoaded', () => {
    renderBooks();
    renderLibrary();
});
  
