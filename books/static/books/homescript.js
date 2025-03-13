document.addEventListener("DOMContentLoaded", () => {
    const searchInput = document.getElementById("searchInput");
    const searchBox = document.querySelector(".searchBox");
    const resultsContainer = document.getElementById("resultsContainer");

    // Function to handle the search
    const performSearch = () => {
        const query = searchInput.value.trim();
        
        if (query.length > 0) {
            fetch(`?q=${query}`, {
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                },
            })
            .then(response => response.json())
            .then(data => {
                const subjects = data.subjects;
                let resultsHTML = "<h2>Results</h2><ul>";
                if (subjects.length > 0) {
                    subjects.forEach(subject => {
                        resultsHTML += `
                            <li>
                                <a href="${subject.folder_path}">${subject.name} (${subject.code})</a>
                            </li>
                        `;
                    });
                } else {
                    resultsHTML += "<li>No subjects found</li>";
                }
                resultsHTML += "</ul>";
                resultsContainer.innerHTML = resultsHTML;
            });
        } else {
            resultsContainer.innerHTML = "";
        }
    };

    // Trigger the search on input change (typing)
    searchInput.addEventListener("input", function () {
        performSearch();
    });

    // Trigger the search on Enter key press
    searchInput.addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
            performSearch();
        }
    });

    // Show search button when input is focused
    if (searchInput.value.trim() !== "") {
        searchBox.classList.add("showButton", "instant");
    }
    searchInput.addEventListener("focus", () => {
        searchBox.classList.add("showButton");
        searchBox.classList.remove("instant");
    });
});
 