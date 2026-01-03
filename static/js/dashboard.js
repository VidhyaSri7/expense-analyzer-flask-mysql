document.addEventListener("DOMContentLoaded", function () {

    const dataTag = document.getElementById("expense-data");
    if (!dataTag) return;

    const data = JSON.parse(dataTag.textContent);

    const categories = data.categories || [];
    const totals = data.totals || [];

    if (categories.length === 0 || totals.length === 0) {
        document.getElementById("noData").style.display = "block";
        return;
    }

    const ctx = document.getElementById("expenseChart").getContext("2d");

    new Chart(ctx, {
        type: "pie",
        data: {
            labels: categories,
            datasets: [{
                data: totals,
                backgroundColor: [
                    "#ff6b6b",
                    "#4dabf7",
                    "#ffd43b",
                    "#69db7c",
                    "#9775fa",
                    "#ffa94d"
                ]
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: "bottom"
                }
            }
        }
    });
}); 