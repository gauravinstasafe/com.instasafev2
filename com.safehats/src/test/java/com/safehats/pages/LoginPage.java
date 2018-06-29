package com.safehats.pages;

import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Action;
import org.openqa.selenium.interactions.Actions;

public class LoginPage {

public static void main(String arr[]) throws InterruptedException{	
 System.setProperty("webdriver.chrome.driver","D:\\software\\chromedriver.exe");
 WebDriver driver = new ChromeDriver();
 driver.get("https://www.bigbasket.com");
 driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
 //driver.manage().window().maximize();
 WebElement drop = driver.findElement(By.xpath(".//a[@class='dropdown-toggle meganav-shop']"));
 WebElement drop1 = driver.findElement(By.xpath(".//a[@ng-href='/cl/snacks-branded-foods/?nc=nb']"));
 WebElement drop2 = driver.findElement(By.xpath(".//a[@class='dropdown-toggle meganav-shop']"));
 WebElement drop3 = driver.findElement(By.xpath(".//input[@qa='searchBar']"));
 WebElement search = driver.findElement(By.xpath(".//button[@class='btn btn-default bb-search']"));
 System.out.println("before action");
 Actions builder = new Actions(driver);
 builder.moveToElement(drop).click().perform();
 System.out.println("after select dropdown action");
 Thread.sleep(3000);
 System.out.println("before hold");
 Action act = builder.clickAndHold(drop1).moveToElement(drop2).moveToElement(drop3).release().build();
 act.perform();
// Thread.sleep(3000);
 //System.out.println("after hold action");
 //builder.moveToElement(drop3).perform();
 //Thread.sleep(3000);
 //builder.release().perform();
 //Thread.sleep(3000);
 //search.click();
 System.out.println("after relese");
 Thread.sleep(3000);
 driver.quit();
}}
