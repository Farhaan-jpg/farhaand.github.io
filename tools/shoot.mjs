import { chromium } from 'playwright'

const [, , outName = 'shot', wArg = '1440', hArg = '900', targetY = '0'] = process.argv
const width = Number(wArg)
const height = Number(hArg)
const destY = Number(targetY)

const browser = await chromium.launch()
const page = await browser.newPage({ 
  viewport: { width, height }, 
  deviceScaleFactor: 1
})

await page.goto(process.env.SITE || 'http://localhost:3000', { waitUntil: 'networkidle' })
await page.evaluate(() => document.fonts.ready)
await page.waitForTimeout(1000)

// Scroll incrementally with mouse wheel to trigger all whileInView animations
let currentY = 0
while (currentY < destY) {
  const step = Math.min(250, destY - currentY)
  await page.mouse.wheel(0, step)
  currentY += step
  await page.waitForTimeout(120)
}

await page.waitForTimeout(1800)
await page.screenshot({ path: `tools/out/${outName}.png` })
await browser.close()
console.log('shot ->', `tools/out/${outName}.png`)
