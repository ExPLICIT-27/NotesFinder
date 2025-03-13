document.addEventListener("DOMContentLoaded", function () {
    const lockIconSpan = document.getElementById("lock");  
    const passwordField = document.querySelector("input[name='password']");
    const lockIcon = lockIconSpan.querySelector("ion-icon"); 

    lockIconSpan.addEventListener("mouseover", function() {
        passwordField.type = "text"; 
        lockIcon.setAttribute("name", "lock-open"); 
    });

    lockIconSpan.addEventListener("mouseout", function() {
        passwordField.type = "password"; 
        lockIcon.setAttribute("name", "lock-closed"); 
    });
});

// Auto-dismiss messages after 5 seconds
document.addEventListener('DOMContentLoaded', function() {
    const messages = document.querySelectorAll('.message');
    
    if (messages.length > 0) {
        setTimeout(function() {
            messages.forEach(function(message) {
                message.style.opacity = '0';
                message.style.transform = 'translateY(-10px)';
                message.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
                
                setTimeout(function() {
                    message.remove();
                }, 500);
            });
        }, 2000); 
    }
});

