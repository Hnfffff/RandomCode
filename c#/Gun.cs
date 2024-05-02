using System.Collections;
using System.Collections.Generic;
using System.Linq;
using TMPro.EditorUtilities;
using UnityEngine;

public class Gun : MonoBehaviour
{
    [SerializeField]//Setting up Variables for the Inspector
    [Header("Bullet Properties")]
    public int bulletAmount = 1; //Amount of Projectiles the Gun shoots
    public float bulletDistance = 1; //Distance the gun Shoots
    public GameObject bulletDecal; //Bullet Impact Decal
    public float bulletSpread = 0.1f;


    Ray bullet; // Raycast Bullet (can be called Later)
    RaycastHit bulletHitPos; // Stores the data from where the Raycast Landed
    public int magazineAmmunation = 0; //Amount of bullets in the Magazine
    public int magazineSize = 15; //Size of the Magazine
    public int reserveAmmo = 0; //How much ammo you have in Reserve
    public int maxReserveAmmo = 300;
    public float reloadTime = 1f; //Time it takes for the Gun to Reload
    private bool isReloading = false; //Is the gun Reloading?
    public float shotCooldown = 1f; //How long before the gun can shoot again (Longer means 
    private bool onCooldown = false;

    public string gunCategory;

    public float bulletDamage = 1f;

    public Transform gunPos; //Where the bullets are coming out from

    public Transform camTransform; //Angle of the Camera

    public TMPro.TMP_Text reloadText;

    public Vector3 spread;

    // Start is called before the first frame update
    void Start() //Called when the scene/Program starts
    {
        magazineAmmunation = magazineSize; //Set Magazine bullet amount to the Magazine Size
        reserveAmmo = maxReserveAmmo - magazineAmmunation;
        reloadText.text = $"Ammo: {magazineAmmunation}/ {reserveAmmo}";
    }
    // Update is called once per frame
    void Update()//Called Once Per Frame
    {
        if(Input.GetMouseButtonDown(0)) //Get Mouse Imput Down
        {
            if(magazineAmmunation > 0 && !onCooldown) //Check if there is any ammunition in the Magazine
            {
                magazineAmmunation -= 1; //Take 1 Bullet Away
                Shoot(); //Call Shoot Function
            }
        }

        if(magazineAmmunation == 0 && !isReloading)
        {
            StartCoroutine (Reloading());
        }
    }
    private void Shoot() //Shoots a bullet
    {
        spread = camTransform.transform.forward;
        reloadText.text = $"Ammo: {magazineAmmunation}/ {reserveAmmo}";
        Debug.Log(magazineAmmunation);
        //Debug.Log($"Shot {bulletAmount} Bullets!"); //Debug
        foreach (int i in Enumerable.Range( 0, bulletAmount )) //For loop (For each item in range (the amount of bullets the gun shoots)
        {
            spread = spread + camTransform.transform.TransformDirection(new Vector3(Random.Range(-bulletSpread, bulletSpread), Random.Range(-bulletSpread, bulletSpread)));
            if (Physics.Raycast(gunPos.position, spread, out bulletHitPos, bulletDistance)) //Checking if a bullet hits (Shoot from the xyz coordinate of the gun, in the direction of the camera, with a bit of randomness to simulate recoil/spread if it shoots multiple pellets, send the data to be stored in bulletHitPos so it can be used later, shoot the distance of bulletDistance
            {
                if (bulletHitPos.collider.GetComponent<EnemyHealthTest>() != null)
                {
                    bulletHitPos.collider.GetComponent<EnemyHealthTest>().TakeDamage(bulletDamage);
                }
                else
                {
                    Destroy(Instantiate(bulletDecal, bulletHitPos.point + bulletHitPos.normal * 0.0001f, Quaternion.FromToRotation(Vector3.up, bulletHitPos.normal)), 10f); //Bit weird how it looks, but pretty much just creates an object (bulletDecal) at the hit postition of the raycast + the normal of it + a small number so there is no z fighting, rotates it to Vector3.up, and the normal of the hit object (the way that the face of the model is pointing), and then deleting it after 10 seconds so it doesnt destroy the frames if you decide to spray your gun a shitton
                }

                //Debug.Log($"Hit Object!"); //Debugging
            }
        }
        StartCoroutine(ShotCooldown());
    }
    private void Reload()
    {
        if(reserveAmmo >= magazineSize)
        {
           reserveAmmo -= magazineSize;
           magazineAmmunation = magazineSize;
        }
        else
        {
            magazineAmmunation = reserveAmmo;
            reserveAmmo = 0;
        }
    }
    IEnumerator Reloading()
    {
        Debug.Log("Started Reloading");
        isReloading = true; //Set reloading to true
        reloadText.text = "RELOADING"; //Change UI text to show that we are reloading
        yield return new WaitForSeconds(reloadTime); //Wait for reloadTime seconds
        Reload(); //Call Reload Function
        Debug.Log("Finished Reloading"); //Debug
        isReloading=false; //Set isReloading to False
        reloadText.text = $"Ammo: {magazineAmmunation}/ {reserveAmmo}"; //Set the UI text to show the default ammo system

    }
    IEnumerator ShotCooldown()
    {
        onCooldown = true; //Make cooldown True
        yield return new WaitForSeconds(shotCooldown); //Wait for the cooldown before shooting another bullet
        onCooldown=false; //Make cooldown False
    }
    //IEnumerator Recoil()
    //{

    //}
}
