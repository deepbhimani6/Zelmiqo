document.addEventListener("DOMContentLoaded", () => {
  const header = document.querySelector("header");
  if (header) {
    header.style.minHeight = `${header.clientHeight}px`;
  }

  const isDesktop = document.documentElement.classList.contains("desktop");
  const cartDrawer = document.querySelector(isDesktop ? ".dropdown-menu.cart-content" : ".mobile-cart-content-container");
  const cartTitle = cartDrawer?.querySelector(isDesktop ? ".cart.header-Big-Screen" : ".mobile-wrapper-header");

  if (!cartDrawer || !cartTitle) return;

  const calculateCartHeight = () => {
    const cartTotal = cartDrawer.querySelector("li.cart-totals");
    if (!cartTotal) return;

    const heightCalc = window.innerHeight - cartTitle.offsetHeight - cartTotal.offsetHeight;
    cartDrawer.style.setProperty("--cartListHeight", `${Math.max(heightCalc, 0)}px`);
  };

  const scheduleCalc = () => requestAnimationFrame(calculateCartHeight);

  calculateCartHeight();

  new MutationObserver(scheduleCalc).observe(cartDrawer, {
    childList: true,
    subtree: true,
  });

  document.querySelector(".dropdown-toggle.cart-heading")?.addEventListener("click", scheduleCalc);
  window.addEventListener("resize", scheduleCalc);
});
