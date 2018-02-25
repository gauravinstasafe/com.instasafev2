import org.testng.annotations.*;

@Test(groups= {"BeforeAndAfter"})
public class MethodFailure extends BeforeAndAfter  {

    @BeforeClass
    public void beforeEverything() {
        println("@BeforeClass");
    }

    @BeforeMethod
    public void setUp() {
        println("@BeforeMethod");
    }

    @Test
    public void method1() {
        println("@Test 1");
        assert false;
    }

    @Test
    public void method2() {
        println("@Test 2");
    }

    @AfterClass
    public void afterEverything() {
        println("@AfterClass");
    }

    @AfterMethod
    public void tearDown() {
        println("@AfterMethod");
    }
}
