const { test, expect } = require('@playwright/test');

test.describe('Files Section', () => {
  test.beforeEach(async ({ page }) => {
    // Simulate being authenticated by setting localStorage
    await page.goto('http://localhost:5173');
    await page.evaluate(() => {
      localStorage.setItem('isAuthenticated', 'true');
      localStorage.setItem('user', JSON.stringify({ name: 'Test User' }));
    });
    await page.reload();
  });

  test('should display files section when navigated to', async ({ page }) => {
    await page.goto('http://localhost:5173');
    
    // Navigate to files section
    await page.click('text=Arquivos');
    
    // Check that files section is visible
    await expect(page.locator('text=Arquivos')).toBeVisible();
    await expect(page.locator('text=Gerencie seus arquivos pessoais')).toBeVisible();
    await expect(page.locator('text=Selecione arquivos para upload')).toBeVisible();
  });
});