function uploadProfilePic() {
    document.getElementById('profile-pic-form').submit();
}

// Auto-dismiss messages after 5 seconds
document.addEventListener('DOMContentLoaded', function() {
    const messages = document.querySelectorAll('.message');
    
    if (messages.length > 0) {
        setTimeout(function() {
            messages.forEach(function(message) {
                // Add fade-out animation
                message.style.opacity = '0';
                message.style.transform = 'translateY(-10px)';
                message.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
                
                // Remove the message after animation completes
                setTimeout(function() {
                    message.remove();
                }, 500);
            });
        }, 5000); // 5 seconds
    }
});