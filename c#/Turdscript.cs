using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Turdscript : MonoBehaviour
{
    public float life = 5f;// set variable to 5

    private void Awake()//on spawn in
    {

        Destroy(gameObject, life); // destory gameobject after 5 seconbds
    }
}
