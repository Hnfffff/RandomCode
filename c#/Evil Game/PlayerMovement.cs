using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using UnityEngine.SceneManagement;

public class PlayerMovement : MonoBehaviour
{
    [SerializeField] //Setting up Variables i hate deskchecking so much :(
    [Header("Rigidbody")]
    private Rigidbody rb;
    public GameObject self;
    public GameObject Cam;

    private float horizontalMovement;
    private float verticalMovement;

    [Header("Movement")]
    public float walkSpeed = 2f;
    public float sprintspeed = 3f;
    private Vector3 moveDir;
    public float drag = 2f;
    public bool sprinting;
    public bool crouching;
    public GameObject orientation;

    [Header("Jumping")]
    public bool isGrounded;
    public int maxJumps = 1;
    public int jumps;
    public float jumpHeight = 5f;

    public LayerMask layer;

    float playerHeight = 2f;

    [Header("slope")]
    public float maxangle;
    private RaycastHit slopehit;

    [Header("Audio")]
    public AudioSource source;
    public AudioClip clip;

    [Header("throwing items")]
    public Transform throwpoint;
    public GameObject throwobject;
    public float launchVelocity = 10f;
    public Vector3 mousePos;

    [Header("misc shit")]
    public List<string> Inventory = new List<string>();
    public TMP_Text text;
    

    // Start is called before the first frame update
    void Start()
    {
        rb = GetComponent<Rigidbody>(); // getting rigidbody from object
        layer = LayerMask.GetMask("ground"); //set layer as ground
        jumps = maxJumps; //make jumps  = maxjumps
        List<string> Inventory = new List<string>(); //create list (i know i made it twice but it wouldnt work if i only made it once
    }

    private void Update()
    {
        horizontalMovement = Input.GetAxisRaw("Horizontal"); //getting input on the horizontal axis (a is positive and d is negative) and making that into a float value
        verticalMovement = Input.GetAxisRaw("Vertical"); //getting input on the vertical axis (w is positive and s is negative) and making that into a float value

        moveDir = orientation.transform.forward * verticalMovement + orientation.transform.right * horizontalMovement; //move dir algorithm

        SlopeStop();//call function

        MovementStuff(); //call funtion

        Jump(); //call funciton

        Grounded(); //call function

        //Throwitems(); this works i just removed it cos it diddnt fit the final version

        Console.WriteLine(Inventory); // flag

    }

    void MovementStuff()
    {
        if(Input.GetKey("left shift")) //if left shift is pressed down
        {
            sprint(); //call function
        }

        else if (Input.GetKey(KeyCode.LeftControl)) //if left control is pressed down
        {
            crouch(); //call function
        }

        else //else
        {
            walk(); //call function
        }
    }

    void Grounded() //checking if grounded
    {
        isGrounded = Physics.Raycast(transform.position, Vector3.down, playerHeight/2 + 0.1f); //set grounded to true if a raycast collides to the ground. raycast is half the height of the play + 0.1 units long, and is shot from the players position at to the bottom
    }

    void Jump() // the whole double jump thing doesnt really fit in the final version but i cant be asked to remove it so its still in there
    {
        if (Input.GetKeyDown("space")) // if space is pressed 
        {
            if (isGrounded == true) //if bool is true
            {
                jumps = maxJumps; //jumps  = maxjumps
            }
            if(jumps != 0) //if you have jumps left
            {
                rb.AddForce(transform.up * jumpHeight, ForceMode.Impulse); // add impulse force beldo the player
                jumps -= 1; //minus one jump 
            }
            if(jumps ==1)
            {
                source.PlayOneShot(clip); //play sound (scrapped)
            }
        }
    }

    void sprint() //sprint
    {
        rb.AddForce((moveDir.normalized * sprintspeed) / 2f, ForceMode.Acceleration); //add force in the direction your facing , a positive value being forward and negative value being back on vertical, and neg being left and pos being right
        if (Onslope()) // this is slope logic so you dont slide down, no slopes in game but was necessary in earlier versions
        {
            rb.AddForce((Getslopemovedirection() * sprintspeed) / 2f, ForceMode.Acceleration);// add force in the angle of the slope
        }
    }

    void crouch()//crocuh
    {
        rb.AddForce(moveDir.normalized, ForceMode.Acceleration); //add force but with no multiplier cos its slow
        if (Onslope())
        {
            rb.AddForce((Getslopemovedirection()) / 2f, ForceMode.Acceleration);//slope logic
            if (rb.velocity.y > 0) //IF you are not jumoping or falling
            {
                rb.AddForce(Vector3.down * 80f, ForceMode.Force); //make the player force to the ground
            }
        }
    }

    void walk() // same as sprint but with differend addon
    {
        rb.AddForce((moveDir.normalized * walkSpeed) / 2f, ForceMode.Acceleration);
        if (Onslope())
        {
            rb.AddForce((Getslopemovedirection() * walkSpeed) / 2f, ForceMode.Acceleration);
        }
    }


    void SlopeStop()
    {
        if (Onslope() && isGrounded) //if on slope and grounded
        {
            rb.useGravity = false; //dont use gravity (stops player from falling down)
        }
        else 
        { 
            rb.useGravity = true; //use gravity
        }
    }



    private bool Onslope() // if on slope
    {
        if (Physics.Raycast(transform.position, Vector3.down, out slopehit, playerHeight / 2 + 0.3f)) //shoot raycast out, asme as the jump but exports the normal value of the ground
        {
            float angle = Vector3.Angle(Vector3.up, slopehit.normal); // get the angle of the slope from the normal value we got from the raycast
            return angle < maxangle && angle != 1; //set rue or false depending on this equation
        }

        return false; //else return false
    }

    private Vector3 Getslopemovedirection()
    {
        return Vector3.ProjectOnPlane(moveDir, slopehit.normal.normalized); // get the direction you have to move in opn the slope
    }

    void Throwstuff() //unused in final version
    {
        mousePos = Input.mousePosition; //get the mosue postition
        Quaternion throwpos = Quaternion.Euler(mousePos.x, mousePos.y, mousePos.z); //get the position the gameobject will be launched from

        if (Input.GetMouseButtonDown(0)) //if left click
        {
            var _projectile = Instantiate(throwobject, throwpoint.position, throwpoint.transform.rotation); //spawn shit prefab
            Rigidbody shotrb = _projectile.GetComponent<Rigidbody>(); //get the rigidbody of the prefab
            shotrb.AddForce(throwpoint.forward * 10, ForceMode.Impulse); // add force to that rigidbody to launch it;
        }
    }

    void OnCollisionEnter(Collision collision) // if colliding
    {
       if (collision.gameObject.tag == "Enemy") // if tag enemy
        {
            Debug.Log("you suck"); //flag
            SceneManager.LoadScene("death", LoadSceneMode.Single); // go to game over scene
        }

        if (collision.gameObject.tag == "redorb") //if redorb tag
        {
            Debug.Log("added "+ collision.gameObject.name); // flag
            Destroy(collision.gameObject); // destroy the orb gameobject
            Inventory.Add("Red Orb");//add red orb to the inventory list
            manager.allpicked += 1; // increase the all picked up variable from the manager script
            Debug.Log(manager.allpicked); // flag
            StartCoroutine(OrbRed()); // call function
        }

        if (collision.gameObject.tag == "blueorb") // same as red orb just for blue orb
        {
            Debug.Log("added " + collision.gameObject.name);
            Destroy(collision.gameObject);
            Inventory.Add("Blue Orb");
            manager.allpicked += 1;
            Debug.Log(manager.allpicked);
            StartCoroutine(Orbblue());
        }

        if (collision.gameObject.tag == "greenorb") // same as red orb just for green orb
        {
            Debug.Log("added " + collision.gameObject.name);
            Destroy(collision.gameObject);
            Inventory.Add("Green Orb");
            manager.allpicked += 1;
            Debug.Log(manager.allpicked);
            StartCoroutine(orbgreen());

        }


        //red pedistal collision logic
        if (collision.gameObject.tag == "red pedistal") // if tag is red pedistal
        {
            if (Inventory.Contains("Red Orb")) //check if redorb is in the list
            {
                manager.redplaced = true; //bool from manager set to true
                StartCoroutine(RedPedistal()); // call function
            }
        }
        
        if(collision.gameObject.tag == "redpedistal" && !Inventory.Contains("Red Orb")) // if has tag but no orb in inventory
        {
            StartCoroutine(NoOrb()); // call function
        }


        //same as red pedistal logic but for green pedistal
        if (collision.gameObject.tag == "greenped" )
        {
            if(Inventory.Contains("Green Orb"))
            {
                manager.greenplaced = true;
                StartCoroutine(greenPedistal());
            }
        }
        if (collision.gameObject.tag == "greenped" && !Inventory.Contains("Green Orb"))
        {
            StartCoroutine(NoOrb());
        }


        //same as red pedistal logic but for blue pedistal
        if (collision.gameObject.tag == "bluepedistal")
        {
            if (Inventory.Contains("Blue Orb"))
            {
                manager.blueplaced = true;
                StartCoroutine(bluepedistal());
            }
        }

        if (collision.gameObject.tag == "bluepedistal" && !Inventory.Contains("Blue Orb")) // same as red orb but for blue orb
        {
            StartCoroutine(NoOrb()); // call function
        }


        if (collision.gameObject.name == "Door") // if tag is door
        {
            StartCoroutine(Door()); // call function
        }

        if(collision.gameObject.tag == "Exit") // if tag is exit
        {
            SceneManager.LoadScene("win", LoadSceneMode.Single); // load you win scene
        }

        //coroutines
        //all of these are the same logic, make text be something, wait 2 seconds, then  make the text disappear
        IEnumerator Door() //door
        {
            text.text = "The Door is Locked by an Ancient Seal.";//change text
            yield return new WaitForSeconds(2);//wait 2 seconds
            text.text = "";//make no text
        }

        IEnumerator bluepedistal()
        {
            text.text = "Placed Blue Orb";
            yield return new WaitForSeconds(2);
            text.text = "";
        }

        IEnumerator greenPedistal()
        {
            text.text = "Placed Green Orb";
            yield return new WaitForSeconds(2);
            text.text = "";
        }

        IEnumerator RedPedistal()
        {
            text.text = "Placed Red Orb";
            yield return new WaitForSeconds(2);
            text.text = "";
        }

        IEnumerator NoOrb()
        {
            text.text = "You Are Missing the Required Item";
            yield return new WaitForSeconds(2);
            text.text = "";
        }

        IEnumerator orbgreen()
        {
            text.text = "Picked Up Green Orb";
            yield return new WaitForSeconds(2);
            text.text = "";
        }

        IEnumerator OrbRed()
        {
            text.text = "Picked Up Red Orb";
            yield return new WaitForSeconds(2);
            text.text = "";
        }

        IEnumerator Orbblue()
        {
            text.text = "Picked Up BLue Orb";
            yield return new WaitForSeconds(2);
            text.text = "";
        }
    }
}
