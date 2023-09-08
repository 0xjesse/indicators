// JavaScript code for scrolling ticker
document.addEventListener('DOMContentLoaded', function () {
    const tickerList = document.getElementById('ticker-list');
    const tickerItems = tickerList.getElementsByTagName('li');
    let tickerIndex = 0;

    function scrollTicker() {
        if (tickerItems.length > 1) {
            tickerItems[tickerIndex].style.display = 'none';
            tickerIndex = (tickerIndex + 1) % tickerItems.length;
            tickerItems[tickerIndex].style.display = 'inline';
        }
    }

    setInterval(scrollTicker, 2000); // Change ticker every 2 seconds
});
