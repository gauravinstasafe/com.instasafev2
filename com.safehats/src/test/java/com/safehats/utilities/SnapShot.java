package com.safehats.utilities;
import com.safehats.base.IConstants;
import java.io.File;
import org.apache.commons.io.FileUtils;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;

public class SnapShot {
	public static void Shoot(WebDriver driver) throws Exception{

        //Convert web driver object to TakeScreenshot

        TakesScreenshot scrShot =((TakesScreenshot)driver);

        //Call getScreenshotAs method to create image file

                File SrcFile=scrShot.getScreenshotAs(OutputType.FILE);

            //Move image file to new destination

                File DestFile= new File(IConstants.FILEWITHPATH);

                //Copy file at destination

	     FileUtils.copyFile(SrcFile, DestFile);
	}
}
