package com.safehats.base;

/**
 * @author nilima
 */

public interface IConstants
{
	public static final String BASE_URL = "baseUrl";
	public static final int MAX_STALE_ELEMENT_RETRIES = 5;
    public static final String ADMIN_URL = "adminUrlRelativePath";
	public static final String SELLERPORTAL_URL = "sellerPortalUrlRelativePath";
	public static final String PARTNERPORTAL_URL = "partnerPortalUrlRelativePath";
	public static final String CREATEREQUEST_URL = "createServiceRequestRelativePath";
	public static final String TRACKREQUEST_URL = "trackServiceRequestRelativePath";
	public static final String NEWLEADS_URL = "newLeadsRelativePath";
	public static final String TRACKLEADS_URL =  "trackLeadsRelativePath";
	public static final String SEARCHPARTNERS_URL="searchProfServicePartnerPath";
	
	public static final String LOG_LEVEL = "logLevel";
	public static final String HTML_LOGGING = "htmlLogging";
	public static final String LOG_FILE = "logFile";
	public static final String CONFIG_FILE = "configFile";
	public static final String LOCATOR_FILE = "locatorFile";
	public static final String BROWSER = "browser";
	public static final String MYPROFILE_URL = "myProfileRelativePath";
	
	//mongo connection
	public static final String IP="ip";
	public static final String PORT="port";
	public static final String DBNAME="dbname";
	public static final String DBUSERNAME="username";
	public static final String DBPASSWORD="password";
	
	
	// Capabilities
	public static final String VERSION = "version";
	public static final String PLATFORM = "platform";
	
	// remote runs
	public static final String REMOTE_WD_HOST = "remoteWebDriverHost";
	public static final String REMOTE_WD_PORT = "remoteWebDriverPort";
	
	public static final String CAPTURE_SCR_SHOTS_ALWAYS = "CaptureScreenshotsAlways";
	public static final String CAPTURE_SCR_SHOTS = "CaptureScreenshot";

	
	public static final String TIME_OUT_SECONDS = "timeOutSeconds";
	

	public static final String TESTDATA_BASE_URL = "baseUrl";
	public static final String COMPONENT = "component";
	public static final String ENVIORNMENT = "environment";
	public static final String SCOPE = "scope";
	public static final String TESTTYPE = "testtype";
	public static final String RELEASEADDED = "releaseadded";
	public static final String LABELS = "labels";
	public static final String COMMENTS = "comments";
	
	
	
	public static final String TESTDATAFOLDER = "testfilepath";
	public static final String BANNEDKEYWORDFILENAME = "bannedfilename";
	public static final String BANNEDKEYWORDPDFJPG = "bannedfilepdfjpg";
	public static final String QCBYPASSFILENAME = "qcbypassfilename";
	public static final String QCBYPASSFILENAMEINVALID = "qcbypassfilenameinvalid";	
	public static final String BRANDAUTHFILE = "brandauthfilename";
	public static final String BRANDAUTHFILEINVALID = "brandauthfilenameinvalid";


    public static final String TESTDATAFILENAME="filename";
	public static final String TESTSHEETNAME1 = "Sheetname1";
	public static final String TESTSHEETNAME2= "Sheetname2";
	public static final String TESTSHEETNAME3 = "Sheetname3";
	public static final String TESTSHEETNAME4 = "Sheetname4";
	public static final String USERDIRECTORY ="userdirectory";
	
	//SHIELD ADMIN SYSTEM 
	public static final String SHIELDADMINEMAILID = "adminShieldEmailId";
	public static final String SHIELDADMINPASSWORD = "adminShieldPassword";
	public static final String QCBYPASSDB = "ShieldQCBypass";
	public static final String QCBYPASSVALUE = "SHIELD_QC_BYPASS";
	public static final String BRANDAUTHDB = "BrandAuthorization";
	public static final String BRANDAUTHVALUE = "BRAND_AUTH";
	
	
	//SHIELD SYSTEM
	public static final String NEWBRAND = "newbrand";
	public static final String CATEGORY = "Corporate";
	public static final String EXISTINGBRAND = "Nokia-X2";
	public static final String EXISTINGCATEGORY = "Laptops";
	public static final String EXISTINGCATEGORY1 = "Laptop";
	
	
	//Application Related
	public static final String MANAGEBRANDURLRELATIVEPATH="manageBrandUrlRelativePath";
	
	
	//Mongo Collections
	
	public static final String BANNEDKEYWORDRULES="BannedKeywordRules";
	public static final String ABSURDPRICINGDISCOUNT="AbsurdPricingDiscount";

	//screenshot
	
	public static final String FILEWITHPATH = "D:\\workspace\\com.safehats\\reports\\screenshots";
}
