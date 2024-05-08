using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class PlayerJump : MonoBehaviour
{
    Rigidbody rb;
    public float jumpHeight = 1.5f;
    public KeyCode jumpKey = KeyCode.Space;
    public float maxJump = 5f;
    public float minJump = 1f;
    public float jumpCharge;
    public float chargeSpeed = 2.5f;
    public float turnSpeed = 1f;
    public Transform groundCheck;
    public float groundDistance = 0.4f;
    public LayerMask groundMask;
    public Text _charge;
    bool isGrounded;
    public PhysicMaterial pm;

    // Start is called before the first frame update
    void Start()
    {
        rb = GetComponent<Rigidbody>();
        jumpCharge = 1;
    }

    // Update is called once per frame
    void Update()
    {
        Quaternion q = transform.rotation;
        q.eulerAngles = new Vector3(0, q.eulerAngles.y, 0);
        transform.rotation = q;

        _charge.text = "charge: " + jumpCharge;

        isGrounded = Physics.CheckSphere(groundCheck.position, groundDistance, groundMask);

        if(!isGrounded)
        {
            pm.dynamicFriction = 100000000f;
        }


        if(isGrounded)
        {
            q.eulerAngles = new Vector3(q.eulerAngles.x, q.eulerAngles.y, q.eulerAngles.z);
            transform.rotation = q;
        }

        if (Input.GetButton("jumpKey") && jumpCharge < maxJump && isGrounded)
        {
            jumpCharge += chargeSpeed * Time.deltaTime;
            jumpCharge = Mathf.Clamp(jumpCharge, minJump, maxJump);
        }

        if (Input.GetButtonUp("jumpKey") && isGrounded)
        {
            rb.AddForce((Vector3.up + transform.forward).normalized * jumpCharge * jumpHeight, ForceMode.Impulse);
            jumpCharge = 1f;
        }

        if(Input.GetKey(KeyCode.LeftArrow))
        {
            transform.Rotate(0, -turnSpeed, 0);
        }

        if (Input.GetKey(KeyCode.RightArrow))
        {
            transform.Rotate(0, turnSpeed, 0);
        }
    }
}
