# MRT Software Induction Project: Quad-Search Strategy
*Madhav Agrawal*

## Introduction
In this project, I have worked to enhance our existing ArUco tag search strategy for the URC problem statement.

### Problem Statement
Our primary objective is to locate three posts which have GNSS Coordinates, within a 20-meter radius, each marked with a 3-sided marker displaying an ArUco tag. Once detected, our task is to navigate the rover to stop within 2 meters of each post. Therefore, our focus lies on efficiently searching for and identifying the ArUco tags within the specified radius to ensure accurate navigation and positioning of the rover.

### Current Strategy
Currently, we are using square search strategy - in which we move the rover recursively to the vertices of squares and perform a 360 degree rotation. However, this year we will use rotating stereo camera to cut down this rotation effort!!

#### Cons of Current Strategy
Some of the major problems that we will be facing in the current strategy are:

- Accuracy - There might be some chance that some area is left for scanning.
- **Blind spot** - The presence of the pole at the back of the rover creates a blind spot for the rotating stereo-camera, potentially causing it to fail to detect an ArUco tag positioned directly behind the rover.
- **Time** - In the long term, the rotation time required for the stereo-camera mount and the adjustments made to eliminate blind spots are factors that inevitably demand a significant amount of time.

## Solutions
To address the mentioned challenges, I suggest the following solutions to simplify and streamline the process of locating ArUco markers, thus making our task more efficient:

### Strategy - 0: WebCams
In this proposed solution, we aim to utilize 3 or 4 webcams or standard cameras strategically positioned at angles of either 120° or 90° around the rover. This configuration offers a comprehensive view of the rover's surroundings without the need for camera rotation at each step. By eliminating this rotation process, we effectively reduce the time required for scanning and enhance efficiency in detecting ArUco markers.

![Cameras Setup](image1.png)

**Implementation**
- To minimize complexity, we'll connect all cameras to a Raspberry Pi, leveraging its existing presence in rover and available pins. The Raspberry Pi will process webcam feeds to detect ArUco tags silently and compactly, ensuring streamlined operation.
- Upon detecting an ArUco tag, the Raspberry Pi will send a signal to the NUC, the main processing unit, prompting it to rotate the stereo-camera in the tag's direction to capture depth information.
- Simultaneously, the rover will be directed to move towards the tag's location.

**Numbers**
- The webcam's accuracy for ArUco detection is sufficient, delivering reliable results up to a minimum distance of 10 meters.
- Given that each camera costs approximately 1k, the overall cost of 3-4k for all cameras is within a reasonable budget range. Therefore, budget constraints are not a significant issue.

**Pros**
- Reduce the rotation time of camera/rover.
- Provides better range than stereo camera. In case, if we are unable to detect the ArUco marker using stereo-camera, we can still move in the direction in which webcam is detecting it.

**Bonus**
By implementing video stabilization techniques, we can enable the rover to continuously search for ArUco markers without the need to stop, capture images, and detect markers sequentially. This dynamic approach enhances efficiency by allowing the rover to maintain constant movement while actively scanning its surroundings for ArUco markers in real-time, thereby saving valuable time during missions.

### Strategy-1: Square Spiral
In this strategy, we will adopt a square-based spiral movement pattern, pausing for detection at corners or edges based on the radial distance from the center. To get more details, [check out this section](#strategy-1--square-spiral).

### Strategy-2: Circle Circle
This strategy involves searching for ArUco markers by moving in a circular pattern, ensuring comprehensive coverage of the area within two to three rounds. To get more details, [check out this section](#strategy-2--circle-circle).

## Strategy-1: Square Spiral
In this strategy, we will adopt a square-based spiral movement pattern, pausing for detection at corners or edges based on the radial distance from the center.

![Strategy-1 Illustration](image2.png)

In this approach, the rover will traverse along the edges of a square, gradually increasing the edge length at a constant rate, resulting in a spiral trajectory. Figure 2 illustrates an example of this described path.

Based on whether the square index of the edge is even or odd, the rover will stop for detection at corners if the square index is odd, or at points gained after bisecting, trisecting, quadrasacting, etc., the edge, depending on its length.

To see the simulation of the above strategy, check out this [video](#).

**Numbers and Calculations**
Here I have presented some data related to the above strategy which will help to optimize the strategy and making it more efficient.
This strategy has 3 main variables:
- Initial edge length
- Factor determining the rate of increase in square length
- Max iterations (edges)

Which depends on the factors:
- Accuracy of the stereo-camera.
- Search range which is 20 m.

**Pros**
**Cons**

## Strategy-2: Circle Circle

## Some examples to get started
### How to create Sections and Subsections
Simply use the section and subsection commands, as in this example document! With Overleaf, all the formatting and numbering are handled automatically according to the template you've chosen. If you're using the Visual Editor, you can also create new sections and subsections via the buttons in the editor toolbar.

### How to include Figures
First, you have to upload the image file from your computer using the upload link in the file-tree menu. Then use the includegraphics command to include it in your document. Use the figure environment and the caption command to add a number and a caption to your figure. See the code for Figure 1 in this section for an example.

Note that your figure will automatically be placed in the most appropriate place for it, given the surrounding text and taking into account other figures or tables that may be close by. You can find out more about adding images to your documents in this help article on [including images on Overleaf](https://www.overleaf.com/learn/how-to/Including_images_on_Overleaf).

### How to add Tables
Use the table and tabular environments for basic tables --- see Table 1, for example. For more information, please see this help article on [tables](https://www.overleaf.com/learn/latex/tables).

### How to add Comments and Track Changes
Comments can be added to your project by highlighting some text and clicking "Add comment" in the top right of the editor pane. To view existing comments, click on the Review menu in the toolbar above. To reply to a comment, click on the Reply button in the lower right corner of the comment. You can close the Review pane by clicking its name on the toolbar when you're done reviewing for the time being.

Track changes are available on all our [premium plans](https://www.overleaf.com/user/subscription/plans), and can be toggled on or off using the option at the top of the Review pane. Track changes allow you to keep track of every change made to the document, along with the person making the change.

### How to add Lists
You can make lists with automatic numbering...
- Like this,
- and like this.

...or bullet points...
- Like this,
- and like this.

### How to write Mathematics
LaTeX is great at typesetting mathematics. Let $X_1, X_2, \ldots, X_n$ be a sequence of independent and identically distributed random variables with $E[X_i] = \mu$ and $Var[X_i] = \sigma^2 < \infty$, and let
$$S_n = \frac{X_1 + X_2 + \cdots + X_n}{n}
      = \frac{1}{n}\sum_{i}^{n} X_i$$
denote their mean. Then as $n$ approaches infinity, the random variables $\sqrt{n}(S_n - \mu)$ converge in distribution to a normal $\mathcal{N}(0, \sigma^2)$.

### How to change the margins and paper size
Usually the template you're using will have the page margins and paper size set correctly for that use-case. For example, if you're using a journal article template provided by the journal publisher, that template will be formatted according to their requirements. In these cases, it's best not to alter the margins directly.

If however you're using a more general template, such as this one, and would like to alter the margins, a common way to do so is via the geometry package. You can find the geometry package loaded in the preamble at the top of this example file, and if you'd like to learn more about how to adjust the settings, please visit this help article on [page size and margins](https://www.overleaf.com/learn/latex/page_size_and_margins).

### How to change the document language and spell check settings
Overleaf supports many different languages, including multiple different languages within one document.

To configure the document language, simply edit the option provided to the babel package in the preamble at the top of this example project. To learn more about the different options, please visit this help article on [international language support](https://www.overleaf.com/learn/latex/International_language_support).

To change the spell check language, simply open the Overleaf menu at the top left of the editor window, scroll down to the spell check setting, and adjust accordingly.

### How to add Citations and a References List
You can simply upload a .bib file containing your BibTeX entries, created with a tool such as JabRef. You can then cite entries from it, like this: [@greenwade93]. Just remember to specify a bibliography style, as well as the filename of the .bib. You can find a [video tutorial here](https://www.overleaf.com/help/97-how-to-include-a-bibliography-using-bibtex) to learn more about BibTeX.

If you have an [upgraded account](https://www.overleaf.com/user/subscription/plans), you can also import your Mendeley or Zotero library directly as a .bib file, via the upload menu in the file-tree.

### Good luck!
We hope you find Overleaf useful, and do take a look at our [help library](https://www.overleaf.com/learn) for more tutorials and user guides! Please also let us know if you have any feedback using the Contact Us link at the bottom of the Overleaf menu --- or use the contact form at [https://www.overleaf.com/contact](https://www.overleaf.com/contact).
