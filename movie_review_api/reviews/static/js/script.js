document.addEventListener("DOMContentLoaded", () => {
    // Handle review form submission
    const reviewForm = document.getElementById("review-form");
    if (reviewForm) {
        reviewForm.addEventListener("submit", (event) => {
            event.preventDefault();

            const movieName = document.getElementById("movie_name").value;
            const reviewText = document.getElementById("review_text").value;
            const rating = document.getElementById("rating").value;

            const formData = {
                movie_name: movieName,
                review_text: reviewText,
                rating: rating,
            };

            fetch("/api/reviews/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(formData),
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert("Review added successfully!");
                    window.location.href = "/"; // Redirect to homepage or review list
                } else {
                    alert("Failed to add review");
                }
            })
            .catch(error => console.error("Error:", error));
        });
    }
});
