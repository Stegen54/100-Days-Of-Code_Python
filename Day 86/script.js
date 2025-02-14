
const ADMIN_USERNAME = 'admin';
const ADMIN_PASSWORD = 'password123';

let isLoggedIn = false;

function showLoginForm() {
    document.getElementById('loginForm').classList.toggle('hidden');
}

function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    if (username === ADMIN_USERNAME && password === ADMIN_PASSWORD) {
        isLoggedIn = true;
        document.getElementById('loginForm').classList.add('hidden');
        document.getElementById('loginBtn').style.display = 'none';
        document.getElementById('auth-buttons').innerHTML = `
            <button onclick="logout()">Logout</button>
        `;
        document.getElementById('newPost').classList.remove('hidden');
        loadPosts();
    } else {
        alert('Invalid credentials');
    }
}

function logout() {
    isLoggedIn = false;
    document.getElementById('loginBtn').style.display = 'block';
    document.getElementById('auth-buttons').innerHTML = `
        <button id="loginBtn" onclick="showLoginForm()">Login</button>
    `;
    document.getElementById('newPost').classList.add('hidden');
    loadPosts();
}

function submitPost() {
    const title = document.getElementById('postTitle').value;
    const content = document.getElementById('postContent').value;
    const timestamp = new Date().toISOString();

    if (!title || !content) {
        alert('Please fill in both title and content');
        return;
    }

    const posts = JSON.parse(localStorage.getItem('blog_posts') || '[]');
    posts.unshift({
        title,
        content,
        timestamp
    });

    localStorage.setItem('blog_posts', JSON.stringify(posts));
    document.getElementById('postTitle').value = '';
    document.getElementById('postContent').value = '';
    loadPosts();
}

function loadPosts() {
    const posts = JSON.parse(localStorage.getItem('blog_posts') || '[]');
    const postsContainer = document.getElementById('posts');
    postsContainer.innerHTML = '';

    posts.forEach(post => {
        const date = new Date(post.timestamp).toLocaleDateString();
        const postElement = document.createElement('div');
        postElement.className = 'post';
        postElement.innerHTML = `
            <h2>${post.title}</h2>
            <small>${date}</small>
            <p>${post.content}</p>
            ${isLoggedIn ? `<button onclick="deletePost('${post.timestamp}')">Delete</button>` : ''}
        `;
        postsContainer.appendChild(postElement);
    });
}

function deletePost(timestamp) {
    if (!isLoggedIn) return;
    
    let posts = JSON.parse(localStorage.getItem('blog_posts') || '[]');
    posts = posts.filter(post => post.timestamp !== timestamp);
    localStorage.setItem('blog_posts', JSON.stringify(posts));
    loadPosts();
}

// Load posts when the page loads
document.addEventListener('DOMContentLoaded', loadPosts);