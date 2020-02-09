using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NPC : Enemy {

    public Transform target;
    public float chaseRadius;
    public float attackRadius;
    //public float moveSpeed;
    private Rigidbody2D myRigidbody;
    private Animator animator;


    public Transform homePosition;

	// Use this for initialization
	void Start () {
        animator = GetComponent<Animator>();
        target = GameObject.FindWithTag("Player").transform;
    }

    // Update is called once per frame
    void Update () {
        CheckDistance();
	}

    void CheckDistance()
    {
        if (Vector3.Distance(target.position, transform.position) <= chaseRadius &&
            Vector3.Distance(target.position, transform.position) > attackRadius)
        {
            transform.position = Vector3.MoveTowards(transform.position, target.position, moveSpeed * Time.deltaTime);
            float change_x = target.position.x - transform.position.x;
            float change_y = target.position.y - transform.position.y;

            animator.SetFloat("moveX", change_x);
            animator.SetFloat("moveY", change_y);
            animator.SetBool("moving", true);
        }
        else
        {
            animator.SetFloat("moveX", 0f);
            animator.SetFloat("moveY", 0f);
            animator.SetBool("moving", false);
        }
    }
}
