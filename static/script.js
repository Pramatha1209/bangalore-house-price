let screens = document.querySelectorAll(".screen");
let current = 0;

let data = {
    location: "",
    sqft: 500,
    bhk: 1,
    floor: 1
};

function nextScreen() {
    screens[current].classList.remove("active");
    current++;
    screens[current].classList.add("active");
}

function updateSqft() {
    let val = document.getElementById("sqftRange").value;
    document.getElementById("sqftValue").innerText = val;
    data.sqft = val;
}

function selectBHK(val) {
    data.bhk = val;
}

function selectFloor(val) {
    data.floor = val;
}

function predict() {
    nextScreen();

    document.getElementById("price").innerText = "AI is thinking...";

    data.location = document.getElementById("locationSelect").value;

    setTimeout(() => {
        fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        })
        .then(res => res.json())
        .then(result => {
            animatePrice(result.price);
        });
    }, 1500);
}

function animatePrice(finalPrice) {
    let count = 0;
    let interval = setInterval(() => {
        count += finalPrice / 20;
        if (count >= finalPrice) {
            count = finalPrice;
            clearInterval(interval);
        }
        document.getElementById("price").innerText = "₹ " + Math.round(count);
    }, 50);
}

function restart() {
    location.reload();
}