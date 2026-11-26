import { registerRoot, Composition } from 'remotion';
import React from 'react';
import { Clip5c } from './Clip5c';
import t from './timing_c5c.json';

const FPS = 30;
const Root = () => (<>
  <Composition id="Clip5c" component={Clip5c} durationInFrames={Math.ceil(t.total * FPS)} fps={FPS} width={1920} height={1080} />
</>);
registerRoot(Root);
