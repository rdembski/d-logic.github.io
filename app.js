document.addEventListener("DOMContentLoaded", function() {
    const root = document.getElementById('root');
    
    root.innerHTML = `
        <h1>Welcome to AI Research App</h1>
        <p>Explore our latest tools and news on AI research.</p>
        <nav>
            <a href="#home">Home</a> |
            <a href="#news">News</a> |
            <a href="#about">About</a> |
            <a href="#tools">Tools</a>
        </nav>
        <div id="content"></div>
    `;
    
    const content = document.getElementById('content');
    
    function navigate() {
        const hash = window.location.hash.substring(1);
        if (hash === "news") {
            content.innerHTML = "<h2>News</h2><p>Latest AI research news...</p>";
        } else if (hash === "about") {
            content.innerHTML = "<h2>About</h2><p>Information about us...</p>";
        } else if (hash === "tools") {
            content.innerHTML = "<h2>Tools</h2><p>AI tools description...</p>";
        } else {
            content.innerHTML = "<h2>Home</h2><p>Welcome to the AI Research App!</p>";
        }
    }
    
    window.addEventListener('hashchange', navigate);
    navigate();
});
