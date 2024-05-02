using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraRotation : MonoBehaviour
{
    [SerializeField] //Setting up Variables
    [Header("Camera")]
    private GameObject mainCamera;
    public GameObject cameraHolder;
    private Vector3 camPos;
    private float newroty;

    [Header("Mouse")]
    public float mouseRoty;
    public float mouseRotx;
    public float sensitivity = 0.1f;

    [Header("Player")]
    public GameObject player;
    public Transform orientation;

    // Start is called before the first frame update
    void Start()
    {
        Cursor.lockState = CursorLockMode.Locked; // locking mouse to centre of screen
        Cursor.visible = false; // making mouse invisible
    }

    // Update is called once per frame
    void Update()
    {
        mouseRoty += (Input.GetAxis("Mouse Y")* sensitivity)/2;  // getting mouse's Y input as a float value
        mouseRotx += (Input.GetAxis("Mouse X")* sensitivity)/2; // getting mouse's x input as a float value

        mouseRoty = Mathf.Clamp(mouseRoty, -90f, 90f); //clamp the rotation so it cant go higher than 90 or lower than -90

        transform.localEulerAngles = new Vector3(-mouseRoty, mouseRotx, 0); //maths shit idk really what it does put if like making the transform into a vector 3
        orientation.transform.localEulerAngles = new Vector3(transform.rotation.x, mouseRotx, transform.rotation.z); // set the cameras rotation to the new vector 3
    }
}
