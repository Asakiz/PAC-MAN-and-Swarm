package Swarm;
import robocode.*;
import static robocode.util.Utils.normalRelativeAngleDegrees;

public class insect extends TeamRobot
{
	int turn=0;
	int leaderDead=0;
	

	public void run() {
	
		while(true) {
			if(leaderDead==1){
				setTurnRadarRight(10000);
			}
			ahead(100);
			if(turn==0){
				turnRight(60);
				turn=1;	
			}
			else
			{
				turnLeft(60);
				turn=0;
			}
			
		
		}
	}
	
	public void onRobotDeath(RobotDeathEvent e){
		if(e.getName().equals("SwarmLeader*")){
			leaderDead=1;
		}
	}

	public void onMessageReceived(MessageEvent e) {
		// Fire at a point
		if (e.getMessage() instanceof Point) {
			Point p = (Point) e.getMessage();
			seekAndDestroy(p);
		}
		
	}
	
	public void seekAndDestroy(Point pos){
		// Calculate x and y to target
		double dx = pos.getX() - this.getX();
		double dy = pos.getY() - this.getY();
		// Calculate angle to target
		double theta = Math.toDegrees(Math.atan2(dx, dy));
		// Turn gun to target
		turnGunRight(normalRelativeAngleDegrees(theta - getGunHeading()));
		// Fire hard!
		fire(2);
		
	}
	/**
	 * onScannedRobot: What to do when you see another robot
	 */
	public void onScannedRobot(ScannedRobotEvent e) {
	
		if(isTeammate(e.getName())){
			back(10);
			turnRight(45);
			
			ahead(100);
		}
		else{
			if(leaderDead==1) {
				double enemyPos=this.getHeading() + e.getBearing();
				double x= getX() + e.getDistance() * Math.sin(Math.toRadians(enemyPos));
				double y= getY() + e.getDistance() * Math.cos(Math.toRadians(enemyPos));
				
				Point enemyPoint= new Point(x, y);
			
				seekAndDestroy(enemyPoint);
			}
			else {
				fire(3);
				back(20);
				turnRight(45);
				ahead(100);
			}
		
			
		}
		
	}

	/**
	 * onHitByBullet: What to do when you're hit by a bullet
	 */
	public void onHitByBullet(HitByBulletEvent e) {
		turnLeft(45);
		
		ahead(100);
	}
	
	/**
	 * onHitWall: What to do when you hit a wall
	 */
	public void onHitWall(HitWallEvent e) {
		turnRight(180);
		ahead(20);
		
	}	
	public void OnHitRobot(HitRobotEvent evnt)
	{
	    if (evnt.getBearing() > -90 && evnt.getBearing() <= 90)
	    {
	        back(100);
			turnRight(90);
			ahead(100);
	    }
	    else
	    {
	        ahead(100);
	    }
	}
}
