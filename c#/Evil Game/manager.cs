using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
public class manager : MonoBehaviour
{
    // Start is called before the first frame update
    [SerializeField] //setupo variables (alot) I HATE DESKCHECKING I HATE DESKCHECKING I HATE DESKCHECKING
    [Header("Bools")]
    public static bool blueplaced;
    public static bool redplaced;
    public static bool greenplaced;
    public bool ghost1spawned;
    public bool ghost2spawned;
    public bool ghost3spawned;
    public static bool allplaced;
    public static int allpicked;

    public GameObject GhostPrefab;
    public GameObject GhostSpawn;
    public GameObject Door;
    public GameObject BlueOrb;
    public GameObject RedOrb;
    public GameObject GreenOrb;

    public TMP_Text Text;
    public TMP_Text bigText;

    private void Start()
    {
        blueplaced = false; //set all the variables to initial variables
        redplaced = false;
        greenplaced = false;
        allplaced = false;
        ghost1spawned = false;
        ghost2spawned = false;
        ghost3spawned = false;
        allpicked = 0;
        Text.text = "";
        bigText.text = "";

    }

    private void Update() //call once a frame
    {
        if(blueplaced == true) //if bool is true
        {
            GameObject Blueplaced = GameObject.Find("placed orbblue"); //fin object in scene caled 'placed orbblue'
            if (ghost1spawned == false) //if bool if false
            {
                BlueOrb.SetActive(true); //make gameobject active
                Instantiate(GhostPrefab, GhostSpawn.transform.position, Quaternion.identity); //spawn in ghost
                ghost1spawned = true; //make bool true

                StartCoroutine(blueorb()); //start function

            }
        }
        if(greenplaced == true) //if bool true
        {
            GameObject Greenplaced = GameObject.Find("placed orbgreen"); //same as above just for a different game object
            if (ghost2spawned == false)
            {
                GreenOrb.SetActive(true);
                Instantiate(GhostPrefab, GhostSpawn.transform.position, Quaternion.identity);
                ghost2spawned = true;
                StartCoroutine(greenorb());
            }
        }
        if(redplaced == true) //same as above just for a different game object
        {
            GameObject Redplaced = GameObject.Find("placed orbred");
            if (ghost3spawned == false)
            {
                RedOrb.SetActive(true);
                Instantiate(GhostPrefab, GhostSpawn.transform.position, Quaternion.identity);
                ghost3spawned = true;
                StartCoroutine(redorb());

            }
        }

        if(blueplaced == true && greenplaced == true && redplaced ==true) //chack if all bools and true
        {
            allplaced = true; //make bool ture
            Destroy(Door); //destory 'door' gameobject
        }

        if(allpicked == 3) //if var  = 3
        {
            StartCoroutine(getout()); //start function
        }

        if(Input.GetKeyDown("escape")) //if key ESC is pressed
        {
            Application.Quit(); //quit application
        }
    }

    IEnumerator blueorb() //blue orb coroutine (fancy timer shit)
    {
        Text.text = "Placed Blue Orb"; //make text on screen say 'placed blue orb'
        yield return new WaitForSeconds(2); //wait for 2 seconds
        Text.text = ""; // make text field empty
    }


    IEnumerator redorb() //same as above but for red orb
    {
        Text.text = "Placed Red Orb";
        yield return new WaitForSeconds(2);
        Text.text = "";
    }

    IEnumerator greenorb() //same as above but for green orb
    {
        Text.text = "Placed Green Orb";
        yield return new WaitForSeconds(2);
        Text.text = "";
    }

    IEnumerator getout() //same as above for mose
    {
        bigText.text = "GET OUT"; //changes different text piece
        yield return new WaitForSeconds(5); //wait 5 seconds
        Text.text = "";
    }

    
}
