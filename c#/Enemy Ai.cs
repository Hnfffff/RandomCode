using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;

public class EnemyAi : MonoBehaviour
{
    //setting up variables
    public static bool isValid;
    public Transform goal;
    public int randomLocation;
    public string s;

    private void Start()
    {
        GetDestination(); //call function
    }

    // Update is called once per frame
    void Update()
    {
        NavMeshAgent agent = GetComponent<NavMeshAgent>(); //get navmeshagent component
        agent.destination = goal.position; // set the destination to the position of the goal object
        if(Vector3.Distance(transform.position, goal.position) <= 5f) //if the distance between the destination and the object this script is attached to is less than 5
        {
            GetDestination();//call function
        }

        if(manager.allpicked == 3)
        {
            goal = GameObject.Find("Player").transform; // make the object fo to the player once all the orbs are picked up
        }

    }

    void GetDestination()
    {
        randomLocation = Random.Range(1, 51); //pick random number between 1-51
        s = randomLocation.ToString();//convert that number to a string
        goal = GameObject.Find(s).transform; //set the variable goal to a gameobject in the scene that has the name 'S'
    }


}
