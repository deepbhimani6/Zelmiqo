document.addEventListener("DOMContentLoaded", () => {
  let header = document.querySelector("header");
  header.style.minHeight = header.clientHeight + "px";
});

document.addEventListener("DOMContentLoaded", () => {
  let cartDrawer;
  let cartTitle;

  if (document.documentElement.classList.contains("desktop")) {
    cartDrawer = document.querySelector(".dropdown-menu.cart-content");
    cartTitle = cartDrawer?.querySelector(".cart.header-Big-Screen");
  } else if (document.documentElement.classList.contains("mobile")) {
    cartDrawer = document.querySelector(".mobile-cart-content-container");
    cartTitle = cartDrawer?.querySelector(".mobile-wrapper-header");
  }

  if (!cartDrawer || !cartTitle) return;

  const calculateCartHeight = () => {
    const cartTotal = cartDrawer.querySelector("li.cart-totals");

    if (!cartTotal) return;

    const heightCalc = window.innerHeight - cartTitle.offsetHeight - cartTotal.offsetHeight;

    cartDrawer.style.setProperty("--cartListHeight", `${Math.max(heightCalc, 0)}px`);
  };

  calculateCartHeight();

  const observer = new MutationObserver(() => {
    requestAnimationFrame(calculateCartHeight);
  });

  observer.observe(cartDrawer, {
    childList: true,
    subtree: true,
  });

  document.querySelector(".dropdown-toggle.cart-heading")?.addEventListener("click", () => {
    requestAnimationFrame(calculateCartHeight);
  });

  window.addEventListener("resize", calculateCartHeight);
});
