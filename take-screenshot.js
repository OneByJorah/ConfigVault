const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    headless: true,
    executablePath: process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH || '/home/onebyjorah/.cache/ms-playwright/chromium-1234/chrome-linux64/chrome'
  });
  const page = await browser.newPage();
  await page.setViewportSize({ width: 1440, height: 900 });
  await page.goto('http://localhost:8103/');
  await page.waitForTimeout(3000);
  await page.screenshot({ path: 'docs/assets/screenshot.png', fullPage: true });
  console.log('Screenshot saved to docs/assets/screenshot.png!');
  await browser.close();
})();
