# Crawler-using-jSoup

### This is just the crawler used in my previous project "Adaptive Recommendation system" using jSoup. 
crawlingSoup.java - Used to crawl data from website 'JAVA WikiBooks' - https://en.wikibooks.org/wiki/Java_Programming and 3 types of folders are created as listed below.Here, Jsoup is used to crwal the data.

textfiles : which will store text files for every indexed page

linknames : which stores links to file names

htmlfiles : stores html code for files

**This file can be called by a servlet in web application to perform Crawling in background :** 

## For example, 

```
@WebServlet("/serveletExample2")
public class serveletExample2 extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public serveletExample2() {
        super();
        // TODO Auto-generated constructor stub
    }
    
   
    public void init(ServletConfig config) throws ServletException {
        super.init(config);
        String initial = config.getInitParameter("initial");
        try {
        	// calls the 'crawl' method from 'crawlingJsoup' class
        	 crawlingJsoup.crawl("",getServletContext().getRealPath("/"));
        }
        catch (Exception e) {
        }
      }
```
