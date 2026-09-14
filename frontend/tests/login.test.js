const { test, expect } = require('@playwright/test');

test.describe('Login Page', () => {
  test('should display login form', async ({ page }) => {
    await page.goto('http://localhost:5173');
    
    // Check if login form is visible
    await expect(page.locator('text=Entrar no Flow AI')).toBeVisible();
    await expect(page.locator('input[placeholder="seu@email.com"]')).toBeVisible();
    await expect(page.locator('input[placeholder="••••••••"]')).toBeVisible();
    await expect(page.locator('button:has-text("Entrar")')).toBeVisible();
  });

  test('should show register link', async ({ page }) => {
    await page.goto('http://localhost:5173');
    
    await expect(page.locator('text=Criar conta')).toBeVisible();
  });

  test('should switch to register mode', async ({ page }) => {
    await page.goto('http://localhost:5173');
    
    await page.click('text=Criar conta');
    
    await expect(page.locator('text=Criar conta')).toBeVisible();
    await expect(page.locator('input[placeholder="Confirmar senha"]')).toBeVisible();
    await expect(page.locator('button:has-text("Criar conta")')).toBeVisible();
  });
});