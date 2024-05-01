using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraFollow : MonoBehaviour
{
    public GameObject cameraHolder; // making variables
    public Vector3 cameraFollow;
    public Quaternion cameraRot;
    // Start is called before the first frame update
    void Start()
    {
        cameraFollow = cameraHolder.transform.position; // set cameraFlollow to a gameobjects position
        cameraRot = cameraHolder.transform.rotation; //set cameraRot to a gameobjects rottion
    }
    // Update is called once per frame
    void Update()
    {
        cameraFollow = cameraHolder.transform.position; // make camera always have holders position
        transform.position = cameraFollow; //make camera follow position
    }
}
